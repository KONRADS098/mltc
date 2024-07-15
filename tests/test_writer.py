import nbformat
import pytest

from mltc.writer import NotebookWriter


class TestNotebookWriter:
    @pytest.fixture()
    def mock_notebook(self):
        """Fixture to create a mock notebook object."""
        return nbformat.v4.new_notebook()

    @pytest.fixture()
    def valid_path(self, tmp_path):
        """Fixture to provide a valid file path using pytest's tmp_path fixture."""
        return tmp_path / "test_notebook.ipynb"

    def test_write_notebook_success(self, mocker, mock_notebook, valid_path):
        """Test successful writing of a notebook."""
        mock_write = mocker.patch("nbformat.write")
        NotebookWriter.write_notebook(mock_notebook, str(valid_path))
        mock_write.assert_called_once()

    def test_write_notebook_oserror(self, mocker, mock_notebook):
        """Test OSError is raised and handled correctly when writing a notebook fails."""
        invalid_path = "/invalid/path/test_notebook.ipynb"
        mocker.patch("nbformat.write", side_effect=OSError("Error writing to file"))
        with pytest.raises(OSError, match="Error writing to file"):
            NotebookWriter.write_notebook(mock_notebook, invalid_path)
