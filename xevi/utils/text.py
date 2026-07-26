import re
import string
import unicodedata

PUNC_ISOLATE_RE = re.compile(r"([?.!,¿])")
SPACES_RE = re.compile(r"\s+")
ALPHA_RE = re.compile(r"^[^\d_\W]+$", re.UNICODE)
QUOTES_MAP = str.maketrans({"”": None, "“": None, "«": None, "»": None, "’": "'"})
PUNC_REMOVE_MAP = str.maketrans({char: None for char in string.punctuation})


def preprocess(
    w: str,
    isolate_punc: bool = True,
    remove_punc: bool = False,
    normalize_quotes: bool = True,
    only_alphabetic: bool = False,
) -> str:
    """Preprocess and clean text with customizable options.

    Args:
        w (str): The input text to clean.
        isolate_punc (bool): If True, adds spaces around punctuation marks (?.!,¿).
        remove_punc (bool): If True, removes all standard punctuation.
        normalize_quotes (bool): If True, unifies curly quotes/guillemets.
        only_alphabetic (bool): If True, keeps only words containing letters
            (supports Fon characters like ɛ, ɔ, ɖ).

    Returns:
        str: The preprocessed text.
    """
    if not w:
        return ""

    if normalize_quotes:
        w = w.translate(QUOTES_MAP)
    if remove_punc:
        w = w.translate(PUNC_REMOVE_MAP)
    if isolate_punc:
        w = PUNC_ISOLATE_RE.sub(r" \1 ", w)
    # delete large spaces
    w = SPACES_RE.sub(" ", w).strip()
    if only_alphabetic:
        w = " ".join(word for word in w.split() if ALPHA_RE.match(word))

    return w


def strip_tones(w: str) -> str:
    """Remove tones and diacritics from a string, keeping the base characters.

    This function decomposes characters into their base forms and combining marks,
    filters out the non-spacing marks (tones), and recomposes them into NFC format.
    Example: 'ɔ́' -> 'ɔ', 'ɛ́' -> 'ɛ'.

    Inspired by and adapted from:

    1. https://github.com/kitihounel/fspell/blob/master/fspell/utils.py
    2. https://github.com/bonaventuredossou/ffr-v1/blob/master/model_train_test/fon_fr.py

    Args:
        w (str): The input string to remove tones from.

    Returns:
        str: The stripped string in NFC normalized form.
    """
    if not w:
        return ""

    s = unicodedata.normalize("NFD", w)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")

    return unicodedata.normalize("NFC", s)
