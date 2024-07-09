import uuid
from pathlib import Path

import nbformat


class NotebookValidator:
    """A class for validating and modifying Jupyter notebooks.

    This class provides methods to add unique IDs to cells in a notebook and validate the notebook's format.

    Raises:
        RuntimeError: If the notebook fails validation checks.
    """

    @staticmethod
    def add_ids_to_cells(notebook: nbformat.NotebookNode) -> nbformat.NotebookNode:
        """Adds a unique 'id' field to each cell in the notebook if it doesn't already have one.

        Args:
            notebook (NotebookNode): A notebook object loaded via nbformat.

        Returns:
            NotebookNode: The modified notebook object with 'id' fields added to each cell.
        """
        for cell in notebook.cells:
            if "id" not in cell.metadata:
                cell.metadata["id"] = str(uuid.uuid4())  # assign a new UUID as the ID
        return notebook

    @staticmethod
    def validate_and_add_ids(path: str) -> nbformat.NotebookNode:
        """Validates the notebook's format and ensures that each cell has a unique 'id' field.

        Raises an error if the notebook cannot be validated.

        Args:
            path (str): The file path to the notebook.

        Returns:
            NotebookNode: The validated and modified notebook object with 'id' fields added to each cell.

        Raises:
            RuntimeError: If the notebook fails validation checks.
        """
        with Path.open(path) as f:
            nb = nbformat.read(f, as_version=4)
            nb = NotebookValidator.add_ids_to_cells(
                nb,
            )  # ensure all cells have an 'id' field
            try:
                nbformat.validate(nb)
            except nbformat.ValidationError:
                err_msg = f"The notebook {path} is incapable of merging due to validation errors."
                raise RuntimeError(err_msg) from None
        return nb
