import os
from src.segmenter import segment_document
from src.indexer import Indexer
from src.data_loader import load_and_process_documents
from src.retriever import Retriever
from src.generator import Generator
from typing import List, Dict, Any, Tuple

def run_rag_pipeline(data_directory: str, k: int = 5):
    """
    Runs the complete RAG pipeline with an interactive query loop.

    Args:
        data_directory (str): The path to the directory containing input corpus files.
        k (int): The number of top relevant chunks to retrieve.
    """
    # 1. Load and process documents
    # load_and_process_documents should now return a list of tuples: (filename, text)
    processed_documents: List[Tuple[str, str]] = load_and_process_documents(data_directory)
    if not processed_documents:
        print("No documents found or processed in the specified directory.")
        return

    # 2. Segment the processed text from all documents, including filename and chunk index
    all_chunks_with_metadata: List[Dict[str, Any]] = []
    for filename, doc_text in processed_documents:
        # Pass filename to segment_document
        chunks_with_metadata = segment_document(doc_text, filename)
        all_chunks_with_metadata.extend(chunks_with_metadata)

    if not all_chunks_with_metadata:
        print("No chunks generated from processed documents.")
        return

    print(f"Segmented documents into {len(all_chunks_with_metadata)} chunks.")

    # 3. Index the chunks with their metadata
    indexer = Indexer()
    indexer.add_chunks(all_chunks_with_metadata) # Pass list of dictionaries
    print(f"Indexed {indexer.index.ntotal} chunks.")

    # 4. Initialize Retriever and Generator
    retriever = Retriever(indexer)
    generator = Generator()

    print("\n--- RAG Pipeline Ready ---")
    print("Enter your queries below.")

    # 5. Start interactive query loop
    while True:
        user_query = input("\nEnter your query (type 'quit' to exit): ")
        if user_query.lower() == 'quit':
            break

        if not user_query:
            print("Please enter a query.")
            continue

        # 6. Retrieve relevant chunks with metadata
        retrieved_contexts_metadata: List[Dict[str, Any]] = retriever.retrieve(user_query, k=k)
        print(f"Retrieved {len(retrieved_contexts_metadata)} relevant chunks.")

        # Extract just the text for the generator (assuming generator only needs text)
        retrieved_contexts_text = [chunk_metadata['text'] for chunk_metadata in retrieved_contexts_metadata]

        # 7. Generate the answer
        answer = generator.generate_answer(user_query, retrieved_contexts_text)

        print("\n--- Final Answer ---")
        print(answer)

if __name__ == '__main__':
    data_dir = "data"

    # Create a dummy data directory and files for testing if they don't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir, exist_ok=True)

    sample_corpus_path = os.path.join(data_dir, "sample_corpus.txt")
    if not os.path.exists(sample_corpus_path):
         with open(sample_corpus_path, 'w', encoding='utf-8') as f:
            f.write("This is a sample document for testing the RAG pipeline. It contains information about the process of segmentation, indexing, retrieval, and generation.")

    # Add another dummy file for testing multiple documents
    another_doc_path = os.path.join(data_dir, "another_document.txt")
    if not os.path.exists(another_doc_path):
        with open(another_doc_path, 'w', encoding='utf-8') as f:
            f.write("This is another document. It discusses different topics, such as natural language processing and machine learning models.")


    print(f"Starting RAG pipeline with documents in directory: {data_dir}")
    run_rag_pipeline(data_dir, k=7)
