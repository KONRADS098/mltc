from pathlib import Path
import click
import nbformat

from mltc.merger import NotebookMerger
from mltc.parser import IndexParser
from mltc.selector import NotebookSelector
from mltc.validator import NotebookValidator


@click.command()
@click.argument("output", type=click.Path(writable=True))
def main(output):
    """
    Command line tool to select and merge Jupyter Notebooks from the 'templates' directory.
    """
    parent_dir = Path(__file__).parent
    directory = parent_dir / "templates"
    notebook_selector = NotebookSelector(directory)

    notebook_selector.display_notebooks()

    indices = click.prompt(
        "Please enter the indices of the notebooks to merge, separated by spaces (e.g. 3 1 2)",
        type=str,
    )

    index_parser = IndexParser(indices)
    selected_indices = index_parser.parse_indices()

    if not selected_indices:
        return

    notebooks = notebook_selector.list_notebooks()

    if any(index < 0 or index >= len(notebooks) for index in selected_indices):
        click.echo("Invalid indices selected.")
        return

    selected_notebooks = [notebooks[idx] for idx in selected_indices]

    validator = NotebookValidator()
    merger = NotebookMerger(validator)

    try:
        merged_notebook = merger.merge_notebooks(selected_notebooks)
    except RuntimeError as e:
        click.echo(e)
        return

    try:
        with open(output, "w") as f:
            nbformat.write(merged_notebook, f)
    except IOError as e:
        click.echo(f"Error writing to file {output}: {e}")
        return

    click.echo(f"Merged notebook saved as {output}")
