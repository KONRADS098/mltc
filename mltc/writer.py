from pathlib import Path

import nbformat


class NotebookWriter:
    """Jupyter notebook writer class.

    This class provides methods to write Jupyter notebooks to file paths.
    """

    @staticmethod
    def write_notebook(notebook: nbformat.NotebookNode, path: str) -> None:
        """Writes the Jupyter notebook to the provided file path.

        Args:
            notebook (nbformat.NotebookNode): The notebook object to be written.
            path (str): The file path where the notebook will be saved.

        Raises:
            OSError: If an error occurs while writing the notebook to file.
        """
        try:
            path_obj = Path(path)
            with path_obj.open("w") as f:
                nbformat.write(notebook, f)
        except OSError as e:
            err_msg = f"Error writing to file {path}: {e}"
            raise OSError(err_msg) from e
