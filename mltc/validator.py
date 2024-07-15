import nbformat


class NotebookValidationError(Exception):
    """Exception raised for notebook validation errors."""

    def __init__(self, message: str) -> None:
        """Initialize the NotebookValidationError with a message."""
        self.message = message
        super().__init__(self.message)


class NotebookValidator:
    """Jupyter notebook validator class.

    This class provides methods to validate Jupyter notebooks based on the Jupyter notebook format schema.
    """

    @staticmethod
    def is_valid(notebook: nbformat.NotebookNode) -> bool:
        """Validates the notebook's adherence to the Jupyter notebook format schema.

        Returns True if the notebook is valid, False otherwise.

        Args:
            notebook (nbformat.NotebookNode): The notebook object.

        Returns:
            bool: True if the notebook is valid, False otherwise.

        Raises:
            NotebookValidationError: If the notebook fails validation checks.
        """
        try:
            nbformat.validate(notebook)
        except nbformat.ValidationError as err:
            err_msg = "The notebook does not conform to the Jupyter notebook format schema."
            raise NotebookValidationError(err_msg) from err
        except (ValueError, AttributeError) as err:
            err_msg = "Invalid input: The provided object is not a valid notebook."
            raise NotebookValidationError(err_msg) from err
        return True
