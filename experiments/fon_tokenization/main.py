import unicodedata
from pathlib import Path

from xevi.utils.lexicon import WEBLexicon
from xevi.tokenize.web import WEBTokenizer

lexicon = WEBLexicon.from_file(Path("lex.txt"), tones=True)
tokenizer = WEBTokenizer(lexicon, tones=True)


def tokenize(text):
    return tokenizer.tokenize(text)


phrases = [
    "Wǎ kpɔ́n! É sɔgbe!",
    "É wá égbé ǎ. É jɛ azɔn.",
    "Xó e a ɖɔ ɖo mɛ ɖě lɛ́ɛ nukɔn ɔ́ nyɔ́ nukún ce mɛ ǎ. A ɖe mì kpò."
]

for phrase in phrases:
    # tokenize
    tokens = tokenize(unicodedata.normalize("NFC", phrase))
    print(f"Original: {phrase} \n Tokens: {tokens}")
