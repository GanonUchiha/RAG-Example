# 🧠 Retrieval-Augmented Generation (RAG) with Segmented Indexing

## 🔖 Project Overview

This project implements a basic Retrieval-Augmented Generation (RAG) pipeline from scratch. It demonstrates how to load and process multiple documents, segment the text corpus into chunks, index the segments using FAISS, retrieve relevant segments based on a user query, and generate a response using a language model (Gemini). The project is built without using frameworks like LangChain, focusing on a ground-up implementation for learning purposes.

## 📦 Tech Stack

| Task            | Library                 | Notes                                      |
| --------------- | ----------------------- | ------------------------------------------ |
| Text processing | `nltk`                  | For sentence tokenization                  |
| Embeddings      | `sentence-transformers` | For turning text into vectors              |
| Vector indexing | `faiss`                 | For fast retrieval                         |
| Language model  | `google.generativeai`   | Use Gemini API for answer generation       |
| Environment variables | `python-dotenv`     | For managing API keys                      |
| Python version  | `3.8+`                  | Keep the code modern and typed if possible |

## 🔧 Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd RAG-Example
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment:**

    *   **Windows:**

        ```bash
        .venv\Scripts\activate
        ```

    *   **macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your Gemini API Key:**

    *   Obtain a Gemini API key from the Google AI Studio.
    *   Create a `.env` file in the root directory of the project.
    *   Add your API key to the `.env` file in the following format:

        ```dotenv
        GEMINI_API_KEY=YOUR_API_KEY
        ```
    *   The project uses `python-dotenv` to load this key.

## ▶️ Usage

1.  **Place your corpus files:** Put the text documents you want to use as the corpus in the `data/` directory. The project supports `.txt` and `.csv` file types.
2.  **Run the RAG pipeline:**

    ```bash
    python run_rag.py
    ```

    The `run_rag.py` script will:
    *   Load and process documents from the `data/` directory.
    *   Segment the corpus into chunks.
    *   Create a FAISS index from the chunk embeddings.
    *   Enter an interactive loop prompting you to enter a query.
    *   Retrieve the most relevant chunks based on your query.
    *   Generate an answer using the Gemini model based on the retrieved context and your query.

    Type 'quit' to exit the interactive query loop.

## 📁 Project Structure

```bash
RAG-Example(root)/
│
├── data/
│   └── *.txt, *.csv             # Raw input documents (multiple files and types supported)
│
├── src/
│   ├── data_loader.py           # Code to load and process documents from directory (handles .txt and .csv)
│   ├── segmenter.py             # Code to split input text into chunks
│   ├── indexer.py             # Embedding and FAISS index creation
│   ├── retriever.py             # Code to query FAISS and get text chunks
│   └── generator.py             # Code to prompt Gemini with query+context
│
├── run_rag.py                   # Orchestrates everything end-to-end with interactive querying
└── requirements.txt             # All dependencies
