from pathlib import Path

import nbformat
import pytest

from mltc.reader import NotebookReader


class TestNotebookReader:
    @classmethod
    def setup_class(cls) -> None:
        Path.mkdir("tests/fixtures", exist_ok=True, parents=True)
        nb = nbformat.v4.new_notebook()
        nb.cells.append(nbformat.v4.new_code_cell("print('Hello World')"))
        with Path.open("tests/fixtures/valid.ipynb", "w") as f:
            nbformat.write(nb, f)
        nb_empty = nbformat.v4.new_notebook()
        with Path.open("tests/fixtures/empty.ipynb", "w") as f:
            nbformat.write(nb_empty, f)
        with Path.open("tests/fixtures/invalid.ipynb", "w") as f:
            f.write("This is not a valid JSON")

    @classmethod
    def teardown_class(cls) -> None:
        Path.unlink("tests/fixtures/valid.ipynb")
        Path.unlink("tests/fixtures/empty.ipynb")
        Path.unlink("tests/fixtures/invalid.ipynb")
        Path.rmdir("tests/fixtures")

    def test_read_valid_notebook(self):
        reader = NotebookReader()
        notebook = reader.read_notebook("tests/fixtures/valid.ipynb")
        assert notebook.cells

    def test_read_invalid_path(self):
        reader = NotebookReader()
        with pytest.raises(FileNotFoundError):
            reader.read_notebook("tests/fixtures/non_existing_notebook.ipynb")

    def test_read_invalid_notebook(self):
        reader = NotebookReader()
        with pytest.raises(nbformat.reader.NotJSONError):
            reader.read_notebook("tests/fixtures/invalid.ipynb")

    def test_read_empty_notebook(self):
        reader = NotebookReader()
        notebook = reader.read_notebook("tests/fixtures/empty.ipynb")
        assert len(notebook.cells) == 0
