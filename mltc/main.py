from pathlib import Path

import click
import nbformat

from mltc.merger import NotebookMerger
from mltc.parser import IndexParser, InvalidIndexError, InvalidInputError
from mltc.reader import NotebookReader
from mltc.selector import NotebookSelector
from mltc.validator import NotebookValidator
from mltc.writer import NotebookWriter


def _select_notebooks(directory: Path) -> list:
    """Display available notebooks and prompt the user for selection.

    Args:
        directory (Path): The directory from which to list notebooks.

    Returns:
        list: A list of selected notebook paths.
    """
    notebook_selector = NotebookSelector(directory)
    notebook_selector.display_notebooks()
    indices = click.prompt(
        "Please enter the indices of the notebooks to merge, separated by spaces (e.g. 3 1 2)",
        type=str,
    )
    index_parser = IndexParser(indices)
    try:
        selected_indices = index_parser.parse_indices()
    except InvalidInputError as e:
        click.echo(f"Invalid input: {e}")
        return []
    except InvalidIndexError as e:
        click.echo(f"Invalid index: {e}")
        return []

    if not selected_indices:
        click.echo("No valid indices selected.")
        return []

    notebooks = notebook_selector.list_notebooks()
    return [notebooks[idx] for idx in selected_indices]


def _read_notebooks(selected_notebooks: list[str]) -> list[nbformat.NotebookNode]:
    """Read the selected notebooks and return a list of notebook objects.

    Args:
        selected_notebooks (list[str]): A list of paths to the selected notebooks.

    Returns:
        list[nbformat.NotebookNode]: A list of notebook objects.
    """
    reader = NotebookReader()
    notebooks = []
    for notebook_path in selected_notebooks:
        try:
            notebook = reader.read_notebook(notebook_path)
            notebooks.append(notebook)
        except FileNotFoundError as e:
            click.echo(f"File not found: {e}")
        except OSError as e:
            click.echo(f"Unexpected error reading notebook {notebook_path}: {e}")
    return notebooks


def _merge_and_save_notebooks(selected_notebooks: list[nbformat.NotebookNode], output_path: Path) -> None:
    """Merge selected notebooks and save the result to a specified path.

    Args:
        selected_notebooks (list[nbformat.NotebookNode]): A list of notebooks to be merged.
        output_path (Path): The path where the merged notebook will be saved.

    Raises:
        RuntimeError: If an error occurs during the merging of notebooks.
        OSError: If an error occurs while writing the merged notebook to file.
    """
    validator = NotebookValidator()
    merger = NotebookMerger(validator=validator)
    writer = NotebookWriter()

    try:
        merged_notebook = merger.merge_notebooks(selected_notebooks)
        writer.write_notebook(merged_notebook, output_path)
        click.echo(f"Merged notebook saved at {output_path}")
    except OSError as e:
        click.echo(f"Error writing to file {output_path}: {e}")
    except Exception as e:  # noqa: BLE001
        click.echo(f"Unexpected error during merging: {e}")


@click.command()
@click.option(
    "--templates-dir",
    default=str(Path(__file__).resolve().parent / "templates"),
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True, resolve_path=True),
    help="Directory containing Jupyter notebook templates.",
)
@click.option(
    "--output-path",
    default=str(Path(__file__).resolve().parent / "mltc.ipynb"),
    type=click.Path(exists=False, writable=True, dir_okay=False, resolve_path=True),
    help="Output path for the merged notebook.",
)
def main(templates_dir: click.Path, output_path: click.Path) -> None:
    """Main function to execute the notebook merging tool.

    Args:
        templates_dir (click.Path): The directory containing notebook templates.
        output_path (click.Path): The path where the merged notebook will be saved.
    """
    templates_dir = Path(templates_dir).resolve()
    output_path = Path(output_path).resolve()

    selected_notebooks = _select_notebooks(templates_dir)
    if not selected_notebooks:
        return

    selected_notebooks = _read_notebooks(selected_notebooks)
    _merge_and_save_notebooks(selected_notebooks, output_path)


if __name__ == "__main__":
    main()
