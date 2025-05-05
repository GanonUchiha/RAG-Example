import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any
import numpy as np
from .indexer import Indexer # Relative import

class Retriever:
    """
    Retrieves relevant text chunks with their metadata from a FAISS index
    based on a query.
    """
    def __init__(self, indexer: Indexer):
        """
        Initializes the Retriever with an Indexer instance.

        Args:
            indexer (Indexer): An instance of the Indexer class containing the FAISS index and chunk metadata.
        """
        self.indexer = indexer
        self.model = indexer.model # Use the same model as the indexer
        self.index = indexer.index
        self.chunk_metadata = indexer.chunk_metadata

    def retrieve(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """
        Retrieves the top-k most relevant chunks with their metadata for a given query.

        Args:
            query (str): The user query.
            k (int): The number of top results to retrieve.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each containing the
                                   retrieved chunk's 'text', 'filename',
                                   and 'chunk_index'.
        """
        if self.index is None:
            print("Error: Index is not built yet.")
            return []

        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding).astype('float32'), k)

        retrieved_chunks_metadata = [self.indexer.get_chunk_by_id(int(idx)) for idx in indices[0] if idx != -1]
        return retrieved_chunks_metadata

    def debug_retrieve(self, query: str, k: int = 5):
        """
        Retrieves and prints the top-k most relevant chunks with metadata for a given query for debugging.

        Args:
            query (str): The user query.
            k (int): The number of top results to retrieve.
        """
        print(f"Debugging retrieval for query: '{query}' with k={k}")
        retrieved_chunks_metadata = self.retrieve(query, k)
        print("Retrieved chunks with metadata:")
        if retrieved_chunks_metadata:
            for i, chunk_metadata in enumerate(retrieved_chunks_metadata):
                print(f"Chunk {i+1}: {chunk_metadata}")
        else:
            print("No chunks retrieved.")

if __name__ == '__main__':
    # Example usage (for testing)
    sample_chunks_with_metadata = [
        {"text": "This is the first chunk about cats.", "filename": "doc1.txt", "chunk_index": 0},
        {"text": "This is the second chunk, it is about dogs.", "filename": "doc1.txt", "chunk_index": 1},
        {"text": "The third chunk talks about something else entirely, like birds.", "filename": "doc2.txt", "chunk_index": 0}
    ]
    indexer = Indexer()
    indexer.add_chunks(sample_chunks_with_metadata)

    retriever = Retriever(indexer)
    query = "Tell me about animals."
    relevant_chunks_metadata = retriever.retrieve(query, k=2)
    print("Retrieved chunks with metadata:")
    for chunk_metadata in relevant_chunks_metadata:
        print(f"- {chunk_metadata}")
