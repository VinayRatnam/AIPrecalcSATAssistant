# AI Precalc & SAT Tutor

This project is an AI-powered chatbot designed to act as a personal tutor for Pre-calculus and SAT preparation. Built using LlamaIndex, OpenAI, and Gradio, it leverages Retrieval-Augmented Generation (RAG) to provide answers grounded in your own homework documents, notes, and study materials.

The chatbot features conversational memory, allowing for follow-up questions, and is assigned the persona of an expert tutor to provide encouraging and helpful explanations.

## ✨ Features

* **Retrieval-Augmented Generation (RAG):** Answers are based on the content of *your* documents, not just the LLM's general knowledge.
* **Conversational Memory:** The chatbot remembers the context of the conversation, allowing for natural follow-up questions.
* **Custom Persona:** A system prompt instructs the AI to act as an expert and encouraging tutor.
* **Simple Web Interface:** A clean, user-friendly chat interface is provided by Gradio.
* **Persistent Knowledge:** The document index is built once and saved to disk for fast startups on subsequent runs.

## 🚀 How It Works

The application follows a simple yet powerful RAG pipeline:

1.  **Ingest & Index:** On the first run, all documents in the `data` directory are loaded, broken into chunks, converted into vector embeddings, and stored in a local vector index in the `storage` directory.
2.  **Retrieve:** When you ask a question, the chatbot searches the index to find the most relevant chunks of text from your documents.
3.  **Synthesize:** The retrieved text chunks are combined with your question and the conversation history. This context is then sent to the OpenAI LLM, which generates a tailored, in-character response.

---

## ⚙️ Getting Started

Follow these steps to get the AI tutor running on your local machine.

### Prerequisites

* Python 3.10 or higher
* An OpenAI API Key

### Step 1: Clone the Repository

First, clone this repository to your local machine:
```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### Step 2: Set Up a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

* **On macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

* **On Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

### Step 3: Install Dependencies

This project requires a few Python packages. Create a file named `requirements.txt` in the root of the project and add the following lines:

```txt
# requirements.txt
llama-index
gradio
python-dotenv
openai
```

Now install all the required packages using pip:
```bash
pip install -r requirements.txt
```

### Step 4: Add Your Homework Documents

Place all your study materials (e.g., `.pdf`, `.docx`, `.txt` files) inside the `data` directory. If this directory doesn't exist, please create it. The chatbot will use these files as its knowledge base.


### Step 5: Set Up Your OpenAI API Key

Your secret API key should never be hard-coded into the script. We'll use a `.env` file to manage it securely.

1.  Create a file named `.env` in the root directory of the project.
2.  Add your OpenAI API key to this file as follows:

    ```env
    # .env file
    OPENAI_API_KEY="sk-YourSuperSecretKeyGoesHere12345"
    ```

**Important:** The `.gitignore` file in this repository is configured to ignore the `.env` file, ensuring your secret key is never committed to GitHub.

---

## ▶️ Running the Application

With the setup complete, you can now launch the chatbot.

1.  **Run the main script from your terminal:**
    ```bash
    python app.py
    ```
    *(Assuming your main Python script is named `app.py`)*

2.  **First-Time Indexing:** The first time you run the script, you will see messages indicating that the index is being created. This process may take a few moments depending on the number of documents. The index will be saved to a new `storage` directory.

3.  **Launch Gradio:** Once the index is ready, the script will launch the Gradio web server. You will see output in your terminal like this:
    ```
    Running on local URL:  [http://127.0.0.1:7860](http://127.0.0.1:7860)
    ```

4.  **Open the Chatbot:** Open the provided URL in your web browser to start chatting with your personal AI tutor!
