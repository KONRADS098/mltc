from pathlib import Path

import click


class NotebookSelector:
    """Facilitates the selection of Jupyter notebooks from a specified directory.

    This class is designed to list and display Jupyter notebooks (.ipynb files) located in a given directory
    and its subdirectories, allowing for an organized selection process based on the directory structure.

    Attributes:
        directory (Path): The directory containing the notebooks. This attribute stores the path
                          as a Path object, facilitating operations on file paths.
    """

    def __init__(self, directory: str) -> None:
        """Initializes the NotebookSelector with the specified directory.

        Args:
            directory (str): The path to the directory where the notebooks are located. The path is
                             converted to a Path object for internal use.
        """
        self.directory = Path(directory)

    def display_notebooks(self) -> None:
        """Displays the available notebooks, grouped by their subdirectories.

        This method organizes notebooks into their respective subdirectories and displays them with
        continuous numbering across all groups. The display format includes the group name (subdirectory)
        followed by the list of notebooks in that group, each prefixed with a unique number.
        """
        notebooks = self.list_notebooks()
        grouped_notebooks = {}
        for notebook in notebooks:
            dir_name = notebook.parent.name
            if dir_name not in grouped_notebooks:
                grouped_notebooks[dir_name] = []
            grouped_notebooks[dir_name].append(notebook)

        notebook_count = 1  # continuous numbering from 1
        for group, files in grouped_notebooks.items():
            click.echo(f"{group.capitalize()}:")
            for file in files:
                click.echo(f"{notebook_count}: {file}")
                notebook_count += 1
            click.echo()  # for readability

    def list_notebooks(self) -> list[str]:
        """Lists all Jupyter notebook files (.ipynb) in the directory and its subdirectories.

        This method searches recursively through the specified directory and its subdirectories to find
        all .ipynb files, compiling a list of their paths. Files located outside the target directory
        are skipped to ensure that only relevant notebooks are included.

        Returns:
            list[Path]: A list of paths to the Jupyter notebooks found within the specified directory
                        and its subdirectories.
        """
        notebooks = []
        for file in self.directory.rglob("*.ipynb"):
            if self.directory in file.parents:
                notebooks.append(file)
            else:
                click.echo(f"Skipping file outside the target directory: {file}")
        return notebooks
