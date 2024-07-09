import nbformat

from mltc.validator import NotebookValidator


class NotebookMerger:
    """Merges multiple Jupyter notebooks into a single notebook.

    This class is responsible for merging the contents of multiple Jupyter notebooks into a single notebook.
    It utilizes a NotebookValidator to ensure that each notebook is valid and to preprocess them before merging.
    The merging process preserves the order of the notebooks as provided in the input list.

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
            nb = self.validator.validate_and_add_ids(notebook_path)
            merged.cells.extend(nb.cells)

        return merged
