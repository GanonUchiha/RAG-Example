import os
import csv
from typing import List, Tuple

def load_and_process_documents(directory_path: str) -> List[Tuple[str, str]]:
    """
    Loads and processes documents from a directory, handling different file types,
    and returns a list of (filename, processed_text) tuples.

    Args:
        directory_path (str): The path to the directory containing input corpus files.

    Returns:
        List[Tuple[str, str]]: A list of tuples, each containing the filename
                                and the processed text string from a document.
    """
    processed_documents: List[Tuple[str, str]] = []
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at {directory_path}")
        return processed_documents

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if filename.endswith(".txt"):
                print(f"Processing text file: {filename}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    document_text = f.read()
                processed_documents.append((filename, document_text))
            elif filename.endswith(".csv"):
                print(f"Processing CSV file: {filename}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    header = next(reader) # Read header row
                    csv_text = ""
                    for row in reader:
                        # Format row with headers
                        row_text = ", ".join([f"{header[i]}: {row[i]}" for i in range(len(row))])
                        csv_text += row_text + ". " # Add a period to help with sentence segmentation
                    processed_documents.append((filename, csv_text))

        except Exception as e:
            print(f"Error reading or processing file {filename}: {e}")

    return processed_documents

if __name__ == '__main__':
    # Example usage (for testing)
    # Create a dummy data directory and files for testing
    test_dir = "test_data_loader"
    os.makedirs(test_dir, exist_ok=True)
    with open(os.path.join(test_dir, "doc1.txt"), "w", encoding="utf-8") as f:
        f.write("This is the first sentence of document one. This is the second sentence.")
    with open(os.path.join(test_dir, "data.csv"), "w", encoding="utf-8") as f:
        f.write("Name,Age,City\nAlice,30,New York\nBob,25,London")

    print(f"Loading and processing documents in directory: {test_dir}")
    processed_docs = load_and_process_documents(test_dir)
    for filename, doc_text in processed_docs:
        print(f"Processed Document from {filename}:\n{doc_text}")

    # Clean up dummy test directory
    # import shutil
    # shutil.rmtree(test_dir)
