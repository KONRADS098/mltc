from pathlib import Path

import click
import pytest

from mltc.selector import NotebookSelector


class TestNotebookSelector:
    @pytest.fixture(scope="class")
    def notebook_selector(self, tmp_path_factory):
        tmp_path = tmp_path_factory.mktemp("notebooks")
        (tmp_path / "subdir1").mkdir()
        (tmp_path / "subdir2").mkdir()
        (tmp_path / "subdir1" / "notebook1.ipynb").write_text("content")
        (tmp_path / "subdir2" / "notebook2.ipynb").write_text("content")
        (tmp_path / "notebook_in_root.ipynb").write_text("content")
        return NotebookSelector(str(tmp_path))

    def test_list_notebooks(self, notebook_selector):
        notebooks = notebook_selector.list_notebooks()
        expected_notebooks_count = 3
        assert len(notebooks) == expected_notebooks_count
        assert all(isinstance(notebook, Path) for notebook in notebooks)
        assert all(notebook.suffix == ".ipynb" for notebook in notebooks)

    def test_display_notebooks(self, notebook_selector, mocker):
        mocker.patch("click.echo")
        notebook_selector.display_notebooks()
        assert click.echo.call_count > 0
