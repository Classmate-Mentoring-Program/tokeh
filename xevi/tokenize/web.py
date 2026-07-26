from nltk.tokenize import wordpunct_tokenize
from nltk.tokenize.api import TokenizerI

from xevi.utils.lexicon import WEBLexicon
from xevi.utils.text import strip_tones


class WEBTokenizer(TokenizerI):
    """
    Word-Expressions-Based (WEB) Tokenizer.

    This tokenizer implements the Word-Expressions-Based tokenization strategy
    specifically designed to address the cultural, structural, and linguistic nuances
    of the Fon language. It leverages a human-crafted or crowdsourced vocabulary
    (WEBLexicon) containing complex multi-word expressions (MWEs).

    The tokenizer handles multi-word units as single atomic tokens by applying
    the "higher word order" principle. If a smaller token is entirely contained
    within a larger, more precise multi-word expression found in the text, the
    smaller token is discarded in favor of the higher-order expression.

    Algorithm Steps:
        1. Scan the text to extract all possible valid words and multi-word
           combinations present in the lexicon (generates candidate list L).
        2. Evaluate candidates based on the Fon linguistic principle: higher word
           orders yield more precise and contextually meaningful expressions.
        3. Filter candidates by inclusion (w ⊂ v): if an expression 'w' is a sub-part
           of a longer expression 'v' at the same position, discard 'w'.
        4. Reconstruct the optimal token sequence in chronological order.

    References:
        Bonaventure F. P. Dossou and Chris C. Emezue. 2021. Crowdsourced
        Phrase-Based Tokenization for Low-Resourced Neural Machine Translation:
        The Case of Fon Language. In Proceedings of the EACL 2021 Workshop on
        African Natural Language Processing (AfricanNLP), pages 1-10.
        arXiv preprint: https://arxiv.org/abs/2103.08052

    Attributes:
        lexicon (WEBLexicon): The lexicon instance containing the target expressions.
        sep (str): Separator used to glue words inside a multi-word token. Default: '_'.
        lower (bool): If True, lowercase the input text before processing. Default: False.
    """

    def __init__(
        self, lexicon: WEBLexicon, *, sep: str = "_", lower: bool = True, tones: bool = False
    ):
        self.tones = tones
        self.lexicon = lexicon
        self.sep = sep
        self.lower = lower

    def tokenize(self, text: str) -> list[str]:
        """Tokenize a string into a list of words and multi-word expressions."""
        if not text:
            return []

        if self.lower:
            text = text.lower()

        if self.tones:
            text = strip_tones(text)

        words = wordpunct_tokenize(text)  # tokenize the text into words and punctuation
        n = len(words)
        L = []  # all possibles words-expressions combinaisons

        for start_idx in range(n):
            max_end = min(start_idx + self.lexicon.max_length, n)
            for end_idx in range(start_idx + 1, max_end + 1):
                sub_sequence = tuple(words[start_idx:end_idx])

                if len(sub_sequence) == 1 or sub_sequence in self.lexicon.expressions:
                    L.append(
                        {
                            "start": start_idx,
                            "end": end_idx,
                            "word": sub_sequence,
                            "order": len(sub_sequence),
                        }
                    )

        # check high-order words or expressions
        L_hat = []
        for w in L:
            has_higher_order = False
            for v in L:
                if w["word"] != v["word"] and v["order"] > w["order"]:
                    if v["start"] <= w["start"] and w["end"] <= v["end"]:
                        has_higher_order = True
                        break

            if not has_higher_order:
                L_hat.append(w)

        # restore order
        L_hat.sort(key=lambda x: x["start"])
        return [self.sep.join(w["word"]) for w in L_hat]


if __name__ == "__main__":
    lexicon = WEBLexicon()
