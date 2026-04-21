# Tokeh

> **Tokeh** est un projet d'apprentissage NLP concret, nommé d'après le *Calao*
> (hornbill), oiseau célèbre pour son cri puissant et distinctif à travers
> l'Afrique de l'Ouest.  
> Le projet met l'accent sur des pipelines NLP propres et bien documentés — du
> texte brut jusqu'aux modèles entraînés — avec une attention particulière à la
> reproductibilité et aux bonnes pratiques.

---

## Objectif du projet

Construire une collection d'utilitaires et d'expériences NLP illustrant un
traitement du langage naturel de bout en bout :

- **Prétraitement du texte** – nettoyage, tokenisation, suppression des mots vides.
- **Embeddings** – construction du vocabulaire, encodage one-hot, TF-IDF.
- **Modélisation** – une hiérarchie de classes de base propre pour des modèles NLP modulaires.

---

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/Classmate-Mentoring-Program/tokeh.git
cd tokeh

# 2. Créer et activer un environnement virtuel (Python 3.11+)
python -m venv .venv
source .venv/bin/activate   # Windows : .venv\Scripts\activate

# 3. Installer le projet et ses dépendances
make install
```

---

## Exemple d'utilisation

```python
from tokeh.preprocessing import clean_text, simple_tokenize, remove_stopwords
from tokeh.embeddings import build_vocab, tfidf_vectorize

# --- Prétraitement -------------------------------------------------------
raw = "The quick brown fox jumps over the lazy dog."
cleaned = clean_text(raw)          # 'the quick brown fox jumps over the lazy dog'
tokens  = simple_tokenize(cleaned) # ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
tokens  = remove_stopwords(tokens) # ['quick', 'brown', 'fox', 'jumps', 'lazy', 'dog']

# --- Embeddings ----------------------------------------------------------
corpus = [tokens, simple_tokenize(clean_text("NLP is fun"))]
vocab  = build_vocab(corpus, min_freq=1)
matrix = tfidf_vectorize(corpus, vocab)
print(matrix)
```

---

## Structure du projet

```
tokeh/
├── tokeh/                  # Paquet source
│   ├── __init__.py
│   ├── preprocessing.py     # Nettoyage du texte, tokenisation
│   ├── embeddings.py        # Représentations vectorielles
│   ├── models/
│   │   ├── __init__.py
│   │   └── base.py          # Classe de base des modèles
│   └── utils.py
│
├── notebooks/              # Notebooks Jupyter d'exploration
│   └── 00_getting_started.ipynb
│
├── data/                   # Non versionné (voir .gitignore)
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── tests/                  # Tests unitaires
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

## Développement

```bash
make test      # Lancer pytest
make lint      # Lancer le linter ruff
make format    # Formater avec black
make notebook  # Démarrer le serveur Jupyter
```