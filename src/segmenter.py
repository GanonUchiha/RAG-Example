from typing import List, Dict, Any
import nltk

# Download the punkt tokenizer if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
except Exception:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except Exception:
    nltk.download('punkt_tab')


def segment_document(text: str, filename: str, max_chunk_size: int = 512, overlap_size: int = 100) -> List[Dict[str, Any]]:
    """
    Splits text into chunks based on sentence boundaries with overlap,
    including filename and chunk index.

    Args:
        text (str): Input text document.
        filename (str): The name of the file being segmented.
        max_chunk_size (int): Max characters per chunk.
        overlap_size (int): Number of characters to overlap between chunks.

    Returns:
        List[Dict[str, Any]]: List of dictionaries, each containing
                               'text', 'filename', and 'chunk_index'.
    """
    sentences = nltk.sent_tokenize(text)
    chunks: List[Dict[str, Any]] = []
    current_chunk_text = ""
    chunk_index = 0

    for sentence in sentences:
        # Check if adding the next sentence exceeds the max chunk size
        if len(current_chunk_text) + len(sentence) + 1 <= max_chunk_size: # +1 for the space
            current_chunk_text += (sentence + " ")
        else:
            # If adding the sentence exceeds the size, add the current chunk and start a new one
            chunks.append({
                'text': current_chunk_text.strip(),
                'filename': filename,
                'chunk_index': chunk_index
            })
            chunk_index += 1
            # Start the new chunk with an overlap from the end of the previous chunk
            overlap = current_chunk_text[-overlap_size:].strip() if len(current_chunk_text) > overlap_size else ""
            current_chunk_text = overlap + " " + sentence + " " if overlap else sentence + " "

    # Add the last chunk if it's not empty
    if current_chunk_text:
        chunks.append({
            'text': current_chunk_text.strip(),
            'filename': filename,
            'chunk_index': chunk_index
        })

    return chunks


if __name__ == '__main__':
    # Example usage (for testing)
    sample_text = "This is the first sentence. This is the second sentence. The third sentence is here."
    sample_filename = "sample.txt"
    segmented_chunks = segment_document(sample_text, sample_filename, max_chunk_size=50)
    for chunk in segmented_chunks:
        print(f"Chunk {chunk['chunk_index']} from {chunk['filename']}: {chunk['text']}")
