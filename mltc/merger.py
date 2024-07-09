import click
import nbformat

from mltc.reader import NotebookReader
from mltc.validator import NotebookValidationError, NotebookValidator


class NotebookMerger:
    """Merges multiple Jupyter notebooks into a single notebook.

    This class is responsible for merging the contents of multiple Jupyter notebooks into a single notebook.

    It utilizes a NotebookReader to read the notebooks before merging, and a NotebookValidator to ensure that each
    notebook is valid and to preprocess them before merging.
    The merging process preserves the order of the notebooks as provided in the input list.

    Attributes:
        reader (NotebookReader): An instance of NotebookReader used for reading the notebooks before merging.
        validator (NotebookValidator): An instance of NotebookValidator used for validating and preprocessing
                                       notebooks before merging.
    """

    def __init__(self, reader: NotebookReader, validator: NotebookValidator) -> None:
        """Initializes the NotebookMerger with a NotebookReader and NotebookValidator.

        Args:
            reader (NotebookReader): The notebook reader to be used for reading the notebooks before merging them.
            validator (NotebookValidator): The notebook validator to be used for validating the notebooks
                                           before merging them.
        """
        self.reader = reader
        self.validator = validator

    def merge_notebooks(self, notebooks: list[str]) -> nbformat.NotebookNode:
        """Merges a list of Jupyter notebooks into a single notebook.

        This method sequentially processes each notebook in the provided list, validates and preprocesses
        it using the NotebookValidator, and then merges their contents into a single notebook. The merged
        notebook is returned in the Jupyter notebook format.

        Args:
            notebooks (list[str]): A list of file paths to the Jupyter notebooks to be merged.

        Returns:
            nbformat.NotebookNode: The merged notebook, represented as a NotebookNode object which is
                                   the standard format for Jupyter notebooks.
        """
        merged = nbformat.v4.new_notebook()
        for notebook_path in notebooks:
            try:
                notebook = self.reader.read_notebook(notebook_path)
                if not self.validator.is_valid(notebook):
                    continue  # Skip this notebook due to validation error

                merged.cells.extend(notebook.cells)
            except FileNotFoundError as err:
                click.echo(f"File not found: {err}")
                continue  # Skip this notebook and proceed with the next one
            except NotebookValidationError as err:
                click.echo(f"Validation error: {err}")
                continue  # Skip this notebook due to validation error
        return merged
