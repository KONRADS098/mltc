import pytest

from mltc.parser import IndexParser, InvalidIndexError, InvalidInputError


class TestIndexParser:
    def test_parse_indices_valid_indices(self):
        indices = "1 3 5"
        parser = IndexParser(indices)
        assert parser.parse_indices() == [0, 2, 4]

    def test_parse_indices_invalid_input(self):
        indices = "1 a 5"
        parser = IndexParser(indices)
        with pytest.raises(InvalidInputError):
            parser.parse_indices()

    def test_parse_indices_invalid_index(self):
        indices = "1 -2 5"
        parser = IndexParser(indices)
        with pytest.raises(InvalidIndexError):
            parser.parse_indices()

    def test_parse_indices_empty_input(self):
        indices = ""
        parser = IndexParser(indices)
        assert parser.parse_indices() == []

    def test_parse_indices_single_index(self):
        indices = "1"
        parser = IndexParser(indices)
        assert parser.parse_indices() == [0]

    def test_parse_indices_duplicate_indices(self):
        indices = "1 3 3 5"
        parser = IndexParser(indices)
        assert parser.parse_indices() == [0, 2, 2, 4]

    def test_parse_indices_large_indices(self):
        indices = "1000000 2000000 3000000"
        parser = IndexParser(indices)
        assert parser.parse_indices() == [999999, 1999999, 2999999]
