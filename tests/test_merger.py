import nbformat
import pytest

from mltc.merger import NotebookMerger
from mltc.validator import NotebookValidationError


class TestNotebookMerger:
    @pytest.fixture()
    def mock_validator(self, mocker):
        return mocker.Mock()

    @pytest.fixture()
    def notebook_merger(self, mock_validator):
        return NotebookMerger(mock_validator)

    def test_merge_empty_list(self, notebook_merger):
        result = notebook_merger.merge_notebooks([])
        assert result.cells == []

    def test_merge_single_notebook(self, notebook_merger, mock_validator):
        notebook = nbformat.v4.new_notebook()
        notebook.cells.append(nbformat.v4.new_code_cell("print('Hello, World!')"))
        mock_validator.is_valid.return_value = True
        result = notebook_merger.merge_notebooks([notebook])
        assert result.cells == notebook.cells

    def test_merge_multiple_notebooks(self, notebook_merger, mock_validator):
        notebook1 = nbformat.v4.new_notebook()
        notebook1.cells.append(nbformat.v4.new_code_cell("print('Notebook 1')"))
        notebook2 = nbformat.v4.new_notebook()
        notebook2.cells.append(nbformat.v4.new_code_cell("print('Notebook 2')"))
        mock_validator.is_valid.return_value = True
        result = notebook_merger.merge_notebooks([notebook1, notebook2])
        assert result.cells == notebook1.cells + notebook2.cells

    def test_invalid_notebook_skipped(self, notebook_merger, mock_validator):
        valid_notebook = nbformat.v4.new_notebook()
        valid_notebook.cells.append(nbformat.v4.new_code_cell("print('Valid Notebook')"))
        invalid_notebook = nbformat.v4.new_notebook()
        mock_validator.is_valid.side_effect = [False, True]
        result = notebook_merger.merge_notebooks([invalid_notebook, valid_notebook])
        assert result.cells == valid_notebook.cells

    def test_file_not_found_error_handled(self, notebook_merger, mock_validator):
        notebook = nbformat.v4.new_notebook()
        mock_validator.is_valid.side_effect = FileNotFoundError("File not found")
        result = notebook_merger.merge_notebooks([notebook])
        assert result.cells == []

    def test_notebook_validation_error_handled(self, notebook_merger, mock_validator):
        notebook = nbformat.v4.new_notebook()
        mock_validator.is_valid.side_effect = NotebookValidationError("Validation error")
        result = notebook_merger.merge_notebooks([notebook])
        assert result.cells == []
