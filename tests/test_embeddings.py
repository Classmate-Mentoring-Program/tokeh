"""Tests unitaires pour tokeh.embeddings."""

from tokeh.embeddings import build_vocab, one_hot_encode, tfidf_vectorize


class TestBuildVocab:
    """Tests pour :func:`tokeh.embeddings.build_vocab`."""

    def test_contains_unk(self):
        vocab = build_vocab([["hello", "world"]])
        assert "<UNK>" in vocab
        assert vocab["<UNK>"] == 0

    def test_includes_all_tokens(self):
        vocab = build_vocab([["hello", "world"], ["hello"]])
        assert "hello" in vocab
        assert "world" in vocab

    def test_min_freq_filters_rare_tokens(self):
        vocab = build_vocab([["hello", "world", "rare"]], min_freq=2)
        assert "hello" not in vocab
        assert "world" not in vocab
        assert "rare" not in vocab

    def test_min_freq_keeps_frequent_tokens(self):
        corpus = [["hello", "world"], ["hello", "world"]]
        vocab = build_vocab(corpus, min_freq=2)
        assert "hello" in vocab
        assert "world" in vocab

    def test_empty_corpus(self):
        vocab = build_vocab([])
        assert vocab == {"<UNK>": 0}


class TestOneHotEncode:
    """Tests pour :func:`tokeh.embeddings.one_hot_encode`."""

    def setup_method(self):
        self.vocab = {"<UNK>": 0, "hello": 1, "world": 2}

    def test_known_token(self):
        vec = one_hot_encode("hello", self.vocab)
        assert vec[1] == 1
        assert sum(vec) == 1

    def test_unknown_token_uses_unk(self):
        vec = one_hot_encode("unknown", self.vocab)
        assert vec[0] == 1
        assert sum(vec) == 1

    def test_vector_length_matches_vocab(self):
        vec = one_hot_encode("world", self.vocab)
        assert len(vec) == len(self.vocab)


class TestTfidfVectorize:
    """Tests pour :func:`tokeh.embeddings.tfidf_vectorize`."""

    def setup_method(self):
        self.vocab = {"<UNK>": 0, "hello": 1, "world": 2}
        self.corpus = [["hello", "world"], ["hello"]]

    def test_output_shape(self):
        matrix = tfidf_vectorize(self.corpus, self.vocab)
        assert len(matrix) == len(self.corpus)
        assert all(len(row) == len(self.vocab) for row in matrix)

    def test_all_values_non_negative(self):
        matrix = tfidf_vectorize(self.corpus, self.vocab)
        assert all(v >= 0 for row in matrix for v in row)

    def test_empty_corpus(self):
        matrix = tfidf_vectorize([], self.vocab)
        assert matrix == []
