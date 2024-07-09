from pathlib import Path

import nbformat


class NotebookReader:
    """Jupyter notebook reader class.

    This class provides methods to read Jupyter notebooks from file paths.
    """

    @staticmethod
    def read_notebook(path: str) -> nbformat.NotebookNode:
        """Reads the Jupyter notebook from the provided file path.

        Args:
            path (str): The file path to the notebook.

        Returns:
            nbformat.NotebookNode: The notebook object.

        Raises:
            FileNotFoundError: If the notebook file does not exist.
            OSError: For other OS related issues.
        """
        path_obj = Path(path)
        if not path_obj.exists():
            err_msg = f"The notebook file {path} does not exist."
            raise FileNotFoundError(err_msg)

        try:
            with path_obj.open() as f:
                return nbformat.read(f, as_version=4)
        except nbformat.reader.NotJSONError as err:
            err_msg = f"Error reading {path}: {err}"
            raise nbformat.reader.NotJSONError(err_msg) from err
        except OSError as err:
            err_msg = f"OS error reading {path}: {err}"
            raise OSError(err_msg) from err
