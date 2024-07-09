from pathlib import Path
import click


class NotebookSelector:
    def __init__(self, directory):
        self.directory = Path(directory)

    def display_notebooks(self):
        """
        Displays available notebooks grouped by their subdirectories.
        The numbering of notebooks will be continuous across groups.
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
