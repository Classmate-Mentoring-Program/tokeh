# Documentation Tokeh

Bienvenue dans la documentation du projet NLP **Tokeh**.

Tokeh est nommé d'après le *Calao* (hornbill), célèbre pour son cri puissant
et distinctif à travers l'Afrique de l'Ouest.  Ce projet fournit une base
modulaire et propre pour expérimenter le traitement du langage naturel en
Python.

---

## Modules

### `tokeh.preprocessing`

Fonctions de nettoyage et de tokenisation du texte brut.

| Fonction | Description |
|---|---|
| `clean_text(text, ...)` | Minuscules, suppression ponctuation, normalisation des espaces. |
| `simple_tokenize(text)` | Découpage sur les espaces. |
| `remove_stopwords(tokens, stopwords)` | Filtrage des mots vides dans une liste de tokens. |

### `tokeh.embeddings`

Utilitaires de représentation vectorielle du texte.

| Fonction | Description |
|---|---|
| `build_vocab(corpus, min_freq)` | Construction d'un vocabulaire mot→indice. |
| `one_hot_encode(token, vocab)` | Vecteur one-hot pour un token donné. |
| `tfidf_vectorize(corpus, vocab)` | Matrice TF-IDF pour un corpus tokenisé. |

### `tokeh.models.base`

Classe de base pour tous les modèles NLP de tokeh.

| Classe | Description |
|---|---|
| `BaseModel` | Classe parente de base. |

### `tokeh.utils`

Utilitaires partagés.

| Fonction | Description |
|---|---|
| `get_logger(name, level)` | Crée un logger Python nommé. |
| `ensure_dir(path)` | Crée un répertoire s'il n'existe pas. |
| `read_text_file(path)` | Lit un fichier texte en chaîne. |

---

## Démarrage rapide

```python
from tokeh.preprocessing import clean_text, simple_tokenize, remove_stopwords
from tokeh.embeddings import build_vocab, tfidf_vectorize

tokens = remove_stopwords(simple_tokenize(clean_text("Bonjour, monde NLP !")))
vocab  = build_vocab([tokens])
matrix = tfidf_vectorize([tokens], vocab)
```

---

## Contribuer

1. Forker le dépôt et créer une branche de fonctionnalité.
2. Exécuter `make install` pour installer toutes les dépendances.
3. Écrire les tests dans `tests/`, puis lancer `make test`.
4. Vérifier le style avec `make lint` et formater avec `make format`.
5. Ouvrir une pull request.
