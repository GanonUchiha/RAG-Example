import faiss
from sentence_transformers import SentenceTransformer
from typing import List, Dict, Any
import numpy as np

class Indexer:
    """
    Handles embedding text chunks and creating a FAISS index,
    storing associated metadata.
    """
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2'):
        """
        Initializes the Indexer with a Sentence Transformer model.

        Args:
            model_name (str): The name of the sentence transformer model to use.
        """
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.chunk_metadata: Dict[int, Dict[str, Any]] = {}
        self.dimension = self.model.get_sentence_embedding_dimension()

    def add_chunks(self, chunks: List[Dict[str, Any]]):
        """
        Adds text chunks with metadata to the index.

        Args:
            chunks (List[Dict[str, Any]]): A list of dictionaries, each
                                          containing 'text', 'filename',
                                          and 'chunk_index'.
        """
        if not chunks:
            return

        # Extract just the text for embedding
        chunk_texts = [chunk['text'] for chunk in chunks]
        embeddings = self.model.encode(chunk_texts)

        if self.index is None:
            self.index = faiss.IndexFlatL2(self.dimension)

        current_id = self.index.ntotal
        self.index.add(np.array(embeddings).astype('float32'))

        for i, chunk in enumerate(chunks):
            self.chunk_metadata[current_id + i] = chunk

    def get_chunk_by_id(self, index_id: int) -> Dict[str, Any]:
        """
        Retrieves a chunk's metadata by its index ID.

        Args:
            index_id (int): The ID of the chunk in the index.

        Returns:
            Dict[str, Any]: A dictionary containing the chunk's 'text',
                            'filename', and 'chunk_index', or an empty
                            dictionary if the ID is not found.
        """
        return self.chunk_metadata.get(index_id, {})

if __name__ == '__main__':
    # Example usage (for testing)
    sample_chunks_with_metadata = [
        {"text": "This is the first chunk.", "filename": "doc1.txt", "chunk_index": 0},
        {"text": "This is the second chunk, it is different.", "filename": "doc1.txt", "chunk_index": 1},
        {"text": "The third chunk talks about something else entirely.", "filename": "doc2.txt", "chunk_index": 0}
    ]
    indexer = Indexer()
    indexer.add_chunks(sample_chunks_with_metadata)
    print(f"Index has {indexer.index.ntotal} vectors.")
    print(f"Chunk metadata for ID 0: {indexer.get_chunk_by_id(0)}")
    print(f"Chunk metadata for ID 1: {indexer.get_chunk_by_id(1)}")
    print(f"Chunk metadata for ID 2: {indexer.get_chunk_by_id(2)}")
    print(f"Chunk metadata for ID 3 (non-existent): {indexer.get_chunk_by_id(3)}")
