from pathlib import Path

import click
import nbformat

from mltc.merger import NotebookMerger
from mltc.parser import IndexParser
from mltc.selector import NotebookSelector
from mltc.validator import NotebookValidator


def _validate_paths(base_dir: Path, *paths: Path) -> bool:
    """Validate multiple paths against a base directory.

    Checks if each path in the provided list of paths is relative to the specified base directory.
    If a path is not relative to the base directory, a message is printed, and the function returns False.

    Args:
        base_dir (Path): The base directory to which the paths should be relative.
        *paths (Path): Variable number of Path objects to be validated.

    Returns:
        bool: True if all paths are relative to the base directory, False otherwise.
    """
    for path in paths:
        if not path.is_relative_to(base_dir):
            click.echo(f"{path} is outside the allowed path of {base_dir}.")
            return False
    return True


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
    selected_indices = index_parser.parse_indices()
    if not selected_indices:
        return []
    notebooks = notebook_selector.list_notebooks()
    if any(index < 0 or index >= len(notebooks) for index in selected_indices):
        click.echo("Invalid indices selected.")
        return []
    return [notebooks[idx] for idx in selected_indices]


def _merge_and_save_notebooks(selected_notebooks: list, output_path: Path) -> None:
    """Merge selected notebooks and save the result to a specified path.

    Args:
        selected_notebooks (list): A list of notebooks to be merged.
        output_path (Path): The path where the merged notebook will be saved.

    Raises:
        RuntimeError: If an error occurs during the merging of notebooks.
        OSError: If an error occurs while writing the merged notebook to file.
    """
    validator = NotebookValidator()
    merger = NotebookMerger(validator)
    try:
        merged_notebook = merger.merge_notebooks(selected_notebooks)
    except RuntimeError as e:
        click.echo(e)
        return
    try:
        with output_path.open("w") as f:
            nbformat.write(merged_notebook, f)
    except OSError as e:
        click.echo(f"Error writing to file {output_path}: {e}")
        return
    click.echo(f"Merged notebook saved at {output_path}")


@click.command()
@click.argument(
    "templates_dir",
    default=str(Path(__file__).resolve().parent / "templates"),
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True, resolve_path=True),
)
@click.argument(
    "output_path",
    default=str(Path(__file__).resolve().parent / "mltc.ipynb"),
    type=click.Path(exists=False, writable=True, dir_okay=False, resolve_path=True),
)
def main(templates_dir: click.Path, output_path: click.Path) -> None:
    """Main function to execute the notebook merging tool.

    Args:
        templates_dir (click.Path): The directory containing notebook templates.
        output_path (click.Path): The path where the merged notebook will be saved.
    """
    templates_dir = Path(templates_dir).resolve()
    output_path = Path(output_path).resolve()
    script_dir = Path(__file__).resolve().parent

    if not _validate_paths(script_dir, templates_dir, output_path):
        return

    selected_notebooks = _select_notebooks(templates_dir)
    if not selected_notebooks:
        return

    _merge_and_save_notebooks(selected_notebooks, output_path)


if __name__ == "__main__":
    main()
