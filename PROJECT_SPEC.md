# 🔖 Project Spec: Implement Retrieval-Augmented Generation (RAG) with Segmented Indexing

## 🧠 Objective

Build a basic, working RAG pipeline from scratch that:

* Segments a corpus (potentially multiple documents) into chunks
* Indexes each chunk using FAISS
* Retrieves relevant chunks based on a user query
* Generates a final response using a language model (e.g., Gemini)

No frameworks like LangChain—this is a "from-the-ground-up" learning-focused project.

---

## 📦 Tech Stack

| Task            | Library                 | Notes                                      |
| --------------- | ----------------------- | ------------------------------------------ |
| Text processing | `nltk`                  | For sentence tokenization                  |
| Embeddings      | `sentence-transformers` | For turning text into vectors              |
| Vector indexing | `faiss`                 | For fast retrieval                         |
| Language model  | `google.generativeai`   | Use Gemini API for answer generation       |
| Python version  | `3.8+`                  | Keep the code modern and typed if possible |

---

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
│   ├── indexer.py               # Embedding and FAISS index creation
│   ├── retriever.py             # Code to query FAISS and get text chunks
│   └── generator.py             # Code to prompt Gemini with query+context
│
├── run_rag.py                   # Orchestrates everything end-to-end with interactive querying
└── requirements.txt             # All dependencies
```

---

## 🔧 Task Breakdown

### ✅ 1. Data Loading and Processing (`data_loader.py`)

* Read in documents from a specified directory (`data/`).
* Handle different file types:
    * `.txt`: Read as plain text.
    * `.csv`: Read using a CSV reader, format each row into a descriptive string including header information (e.g., "Header1: Value1, Header2: Value2").
* Return a list of tuples, where each tuple contains the original filename and the processed text string for a document.

### ✅ 2. Text Segmentation (`segmenter.py`)

* Accept a text string and its filename (provided by the data loader).
* Use `nltk.sent_tokenize` to split into sentences.
* Combine sentences into fixed-size chunks (e.g., ~512 tokens or 3-5 sentences).
* Return a list of chunks, where each chunk is a dictionary including the text, original filename, and its index within the segmented file.

### ✅ 3. Embedding + FAISS Indexing (`indexer.py`)

* Convert the text of each chunk to an embedding using `sentence-transformers` (start with `all-MiniLM-L6-v2`).
* Store these embeddings in a single FAISS index.
* Maintain a `chunk_metadata` dictionary linking the FAISS index position to the chunk's full metadata (text, filename, and chunk index).

### ✅ 4. Query Retrieval (`retriever.py`)

* Accept a user query.
* Encode it to a vector.
* Use FAISS to search for top-k similar segments in the combined index.
* Retrieve and return the full metadata (text, filename, and chunk index) for the matching chunks.

### ✅ 4. Answer Generation (`generator.py`)

* Format the retrieved context and question into a prompt
* Use Gemini API to generate an answer
* Keep the prompt clean and clear (instruction + context + question)

---

## 🔮 Example Output

Given:

> "How do cats communicate with humans?"

And after retrieving chunks like:

* "Cats meow to express needs..."
* "Tail movement can indicate emotion..."

The Gemini model might respond with:

> "Cats communicate through meowing, body language like tail movements, and even purring to signal contentment or request attention."

---

## 🚀 Running the Pipeline

Execute `python run_rag.py` from the project root. The script will load and index documents from the `data/` directory and then enter an interactive loop prompting for user queries. Type 'quit' to exit the loop.
