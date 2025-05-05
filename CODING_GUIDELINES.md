# 🔧 Coding Guidelines for RAG Project

## 👉 General Principles

* **Clarity first**: prioritize readable and understandable code over clever tricks
* **Modularity**: functions should be small and focused on one task
* **Reusability**: write general-purpose components where appropriate
* **Consistency**: follow consistent naming and file structure throughout the project

## 🔹 Language & Style

* Use **Python 3.8+** syntax
* Follow **PEP8** for style and naming
* Use `black` for auto-formatting and `flake8` for linting
* Function names: `snake_case`
* Class names: `PascalCase`
* Constants: `ALL_CAPS`
* Prefer **type hints** for all functions and method signatures

## 🔹 Comments & Docstrings

* Use **docstrings** for all functions and classes
* Follow Google-style docstring format

```python
def segment_document(text: str, max_chunk_size: int = 512) -> List[str]:
    """
    Splits text into chunks based on sentence boundaries.

    Args:
        text (str): Input text document.
        max_chunk_size (int): Max characters per chunk.

    Returns:
        List[str]: List of text segments.
    """
```

* Use **inline comments** sparingly to explain non-obvious logic

## 🔹 Logging

* Use `print()` for simple testing
* For production or scaling: switch to `logging` module with different levels

## 🔹 Project-Specific Rules

* Use relative imports inside `src/`
* Keep each script limited to its role (e.g., no embedding in `retriever.py`)
* Write pure functions whenever possible (no file I/O inside core logic unless necessary)

## 🔹 Testing

* Add simple unit tests in a `tests/` directory (if added later)
* Validate each module (`segmenter`, `indexer`, `retriever`, `generator`) with sample input/output checks
