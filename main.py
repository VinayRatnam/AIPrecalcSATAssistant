import os
import gradio as gr
from dotenv import load_dotenv
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
# Import the necessary components
from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.prompts import ChatMessage, MessageRole

# Load environment variables from .env file
load_dotenv()

# --- 1. LOAD THE LLAMAINDEX INDEX ---
PERSIST_DIR = "./storage"

print("Loading index...")
if not os.path.exists(PERSIST_DIR):
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)

print("✅ Index loaded.")


# --- 2. CREATE THE CHAT ENGINE WITH A SYSTEM PROMPT ---
print("🧠 Creating chat engine with a custom role...")

# Define your custom system prompt
system_prompt = (
    "You are an expert tutor for Pre-calculus and the SAT. "
    "Your role is to help the user understand their homework documents. "
    "Be encouraging, clear, and provide step-by-step explanations. "
    "Do not answer questions outside the scope of the provided documents."
)

# Create a list of chat messages with the system prompt
custom_chat_history = [
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=system_prompt,
    ),
]

# Create the ContextChatEngine
chat_engine = ContextChatEngine.from_defaults(
    retriever=index.as_retriever(),
    chat_history=custom_chat_history,
    verbose=True
)

print("✅ Chat engine created.")


# --- 3. DEFINE THE CHATBOT FUNCTION ---
def predict(message, history):
    response = chat_engine.chat(message)
    return str(response)


# --- 4. LAUNCH THE GRADIO CHAT INTERFACE ---
print("🚀 Launching Gradio UI...")
gr.ChatInterface(
    predict,
    title="Precalc & SAT Tutor 🧑‍🏫",
    description="Ask me questions about your homework. I'll help you understand the concepts.",
    theme="soft"
).launch()