"""Unit tests for tokeh.preprocessing."""

import pytest

from tokeh.preprocessing import clean_text, remove_stopwords, simple_tokenize


class TestCleanText:
    """Tests for :func:`tokeh.preprocessing.clean_text`."""

    def test_lowercase_by_default(self):
        assert clean_text("Hello World") == "hello world"

    def test_removes_punctuation_by_default(self):
        assert clean_text("Hello, World!") == "hello world"

    def test_collapses_whitespace(self):
        assert clean_text("hello   world") == "hello world"

    def test_strips_leading_trailing_whitespace(self):
        assert clean_text("  hello  ") == "hello"

    def test_no_lowercase_when_disabled(self):
        assert clean_text("Hello World", lower=False) == "Hello World"

    def test_keep_punctuation_when_disabled(self):
        result = clean_text("Hello, World!", remove_punctuation=False)
        assert "," in result

    def test_empty_string(self):
        assert clean_text("") == ""


class TestSimpleTokenize:
    """Tests for :func:`tokeh.preprocessing.simple_tokenize`."""

    def test_basic_split(self):
        assert simple_tokenize("hello world") == ["hello", "world"]

    def test_empty_string_returns_empty_list(self):
        assert simple_tokenize("") == []

    def test_single_token(self):
        assert simple_tokenize("tokeh") == ["tokeh"]


class TestRemoveStopwords:
    """Tests for :func:`tokeh.preprocessing.remove_stopwords`."""

    def test_removes_default_stopwords(self):
        tokens = ["the", "quick", "brown", "fox"]
        result = remove_stopwords(tokens)
        assert "the" not in result
        assert "quick" in result
        assert "brown" in result
        assert "fox" in result

    def test_custom_stopwords(self):
        tokens = ["hello", "cruel", "world"]
        result = remove_stopwords(tokens, stopwords={"cruel"})
        assert result == ["hello", "world"]

    def test_empty_tokens(self):
        assert remove_stopwords([]) == []

    def test_no_stopwords_in_input(self):
        tokens = ["tokeh", "nlp", "project"]
        assert remove_stopwords(tokens) == tokens
