import nbformat
import pytest

from mltc.validator import NotebookValidationError, NotebookValidator


class TestNotebookValidator:
    @pytest.fixture()
    def validator(self):
        return NotebookValidator()

    def test_is_valid_valid_notebook(self, validator):
        valid_notebook = nbformat.v4.new_notebook()
        valid_notebook.cells.append(nbformat.v4.new_markdown_cell("# Test"))
        assert validator.is_valid(valid_notebook)

    def test_is_valid_invalid_notebook(self, validator):
        invalid_notebook = nbformat.from_dict(
            {
                "cells": [
                    {
                        "cell_type": "invalid",
                        "metadata": {},
                        "source": ["# Test"],
                    }
                ],
                "metadata": {"language_info": {"name": "python"}},
                "nbformat": 4,
                "nbformat_minor": 2,
            }
        )
        with pytest.raises(NotebookValidationError):
            validator.is_valid(invalid_notebook)

    def test_is_valid_invalid_input(self, validator):
        invalid_input = "invalid"
        with pytest.raises(NotebookValidationError):
            validator.is_valid(invalid_input)

    def test_is_valid_empty_notebook(self, validator):
        empty_notebook = nbformat.v4.new_notebook()
        assert validator.is_valid(empty_notebook)
