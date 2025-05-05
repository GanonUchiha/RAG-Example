# 📖 Documentation Guidelines for RAG Project

## 👉 General Philosophy

* Keep documentation **minimal but useful**
* Aim for **clarity** and **discoverability**: explain how to run, modify, and extend the project
* Update docs alongside code changes

## 🔹 Required Files

### `README.md`

* **Project Overview**: Brief summary of what the project does
* **Setup Instructions**:

  * Python version
  * Virtual environment setup
  * Required installations (`pip install -r requirements.txt`)
* **Usage**:

  * How to run `run_rag.py`
  * Sample input/output
* **Project Structure**: Short explanation of each folder/file
* **Credits/License**: Optional

### `CONTRIBUTING.md` (Optional if solo)

* Guidelines for pull requests (if collaborative)
* Branch naming conventions
* Testing or format requirements before commits

## 🔹 In-code Documentation

* Every function must have a **Google-style docstring**
* Classes should include docstrings describing their purpose and key methods
* Complex logic should be explained with inline comments (but avoid obvious statements)

## 🔹 Additional Tips

* Use markdown formatting for code snippets, file paths, and commands
* Use emoji or icons in docs to make them visually skimmable 🌟
* Link out to external resources (e.g. FAISS docs, Gemini API docs) when helpful

## 🔹 Optional Enhancements

* Add diagram (e.g., pipeline architecture) in `docs/`
* Maintain a `CHANGELOG.md` for version tracking
* Create sample `.ipynb` notebooks in `examples/` for demonstration
