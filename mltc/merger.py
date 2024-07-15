import click
import nbformat

from mltc.validator import NotebookValidationError, NotebookValidator


class NotebookMerger:
    """Merges multiple Jupyter notebooks into a single notebook.

    This class is responsible for merging the contents of multiple Jupyter notebooks into a single notebook.

    It utilizes the NotebookValidator to ensure that each notebook is valid before merging.
    The merging process preserves the order of the notebooks.

    Attributes:
        validator (NotebookValidator): An instance of NotebookValidator used for validating and preprocessing
                                       notebooks before merging.
    """

    def __init__(self, validator: NotebookValidator) -> None:
        """Initializes the NotebookMerger with a NotebookValidator.

        Args:
            validator (NotebookValidator): The notebook validator to be used for validating the notebooks
                                           before merging them.
        """
        self.validator = validator

    def merge_notebooks(self, notebooks: list[nbformat.NotebookNode]) -> nbformat.NotebookNode:
        """Merges a list of Jupyter notebooks into a single notebook.

        This method sequentially processes each notebook in the provided list, validates and preprocesses
        it using the NotebookValidator, and then merges their contents into a single notebook. The merged
        notebook is returned in the Jupyter notebook format.

        Args:
            notebooks (list[nbformat.NotebookNode]): A list of Jupyter notebooks to be merged into a single notebook.

        Returns:
            nbformat.NotebookNode: The merged notebook, represented as a NotebookNode object which is
                                   the standard format for Jupyter notebooks.
        """
        merged = nbformat.v4.new_notebook()
        for notebook in notebooks:
            try:
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
