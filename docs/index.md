# Tokeh Documentation

Welcome to the **Tokeh** NLP project documentation.

Tokeh is named after the *Calao* bird (hornbill), celebrated for its loud,
distinctive call across West Africa.  This project provides a clean, modular
foundation for experimenting with natural language processing in Python.

---

## Modules

### `tokeh.preprocessing`

Functions for cleaning and tokenising raw text.

| Function | Description |
|---|---|
| `clean_text(text, ...)` | Lower-case, remove punctuation, collapse whitespace. |
| `simple_tokenize(text)` | Split on whitespace. |
| `remove_stopwords(tokens, stopwords)` | Filter stop-words from a token list. |

### `tokeh.embeddings`

Utilities for building vector representations of text.

| Function | Description |
|---|---|
| `build_vocab(corpus, min_freq)` | Build a word-to-index vocabulary. |
| `one_hot_encode(token, vocab)` | One-hot vector for a single token. |
| `tfidf_vectorize(corpus, vocab)` | TF-IDF matrix for a tokenised corpus. |

### `tokeh.models.base`

Abstract base class for all tokeh NLP models.

| Class / Method | Description |
|---|---|
| `BaseModel` | Abstract parent class. |
| `BaseModel.fit(X, y)` | Train the model. |
| `BaseModel.predict(X)` | Generate predictions. |
| `BaseModel.save(path)` | Persist model to disk. |
| `BaseModel.load(path)` | Restore model from disk. |

### `tokeh.utils`

Shared helpers.

| Function | Description |
|---|---|
| `get_logger(name, level)` | Create a named Python logger. |
| `ensure_dir(path)` | Create a directory if it does not exist. |
| `read_text_file(path)` | Read a text file to a string. |

---

## Quick Start

```python
from tokeh.preprocessing import clean_text, simple_tokenize, remove_stopwords
from tokeh.embeddings import build_vocab, tfidf_vectorize

tokens = remove_stopwords(simple_tokenize(clean_text("Hello, NLP world!")))
vocab  = build_vocab([tokens])
matrix = tfidf_vectorize([tokens], vocab)
```

---

## Contributing

1. Fork the repository and create a feature branch.
2. Run `make install` to install all dependencies.
3. Write tests in `tests/`, then run `make test`.
4. Lint with `make lint` and format with `make format`.
5. Open a pull request.
