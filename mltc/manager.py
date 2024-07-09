from pathlib import Path

import click


class NotebookManager:
    def __init__(self, directory):
        self.directory = Path(directory)

    def list_notebooks(self):
        """
        Lists all .ipynb files in the specified directory and its subdirectories.
        """
        notebooks = []
        for file in self.directory.rglob("*.ipynb"):
            if self.directory in file.parents:
                notebooks.append(file)
            else:
                click.echo(f"Skipping file outside the target directory: {file}")
        return notebooks
