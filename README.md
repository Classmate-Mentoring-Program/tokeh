# Tokeh

> **Tokeh** is a concrete NLP learning project named after the *Calao* bird
> (hornbill), known for its loud, distinctive call across West Africa.  
> The project focuses on clean, well-documented NLP pipelines — from raw text
> to trained models — with an emphasis on reproducibility and best practices.

---

## Project Goal

Build a collection of NLP utilities and experiments that demonstrate
end-to-end natural language processing:

- **Text preprocessing** – cleaning, tokenisation, stop-word removal.
- **Embeddings** – vocabulary construction, one-hot encoding, TF-IDF.
- **Modelling** – a clean base-class hierarchy for pluggable NLP models.

---

## Install

```bash
# 1. Clone the repository
git clone https://github.com/Classmate-Mentoring-Program/tokeh.git
cd tokeh

# 2. Create and activate a virtual environment (Python 3.11+)
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install the project and its dependencies
make install
```

---

## Usage Example

```python
from tokeh.preprocessing import clean_text, simple_tokenize, remove_stopwords
from tokeh.embeddings import build_vocab, tfidf_vectorize

# --- Preprocessing -------------------------------------------------------
raw = "The quick brown fox jumps over the lazy dog."
cleaned = clean_text(raw)          # 'quick brown fox jumps lazy dog'
tokens  = simple_tokenize(cleaned) # ['quick', 'brown', 'fox', ...]
tokens  = remove_stopwords(tokens) # stop-words removed

# --- Embeddings ----------------------------------------------------------
corpus = [tokens, simple_tokenize(clean_text("NLP is fun"))]
vocab  = build_vocab(corpus, min_freq=1)
matrix = tfidf_vectorize(corpus, vocab)
print(matrix)
```

---

## Project Structure

```
tokeh/
├── tokeh/                  # Source package
│   ├── __init__.py
│   ├── preprocessing.py     # Text cleaning, tokenisation
│   ├── embeddings.py        # Vector representations
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py          # Base model class
│   └── utils.py
│
├── notebooks/              # Jupyter exploration notebooks
│   └── 00_getting_started.ipynb
│
├── data/                   # Never committed (see .gitignore)
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── tests/                  # Unit tests
│   ├── __init__.py
│   ├── test_preprocessing.py
│   └── test_embeddings.py
│
├── docs/                   # Documentation
│   └── index.md
│
├── .gitignore
├── pyproject.toml
├── README.md
└── Makefile
```

---

## Development

```bash
make test      # Run pytest
make lint      # Run ruff linter
make format    # Run black formatter
make notebook  # Launch Jupyter notebook server
```