import nbformat

from mltc.validator import NotebookValidator


class NotebookMerger:
    def __init__(self, validator: NotebookValidator):
        self.validator = validator

    def merge_notebooks(self, notebooks):
        """
        Merges the selected Jupyter notebook files into one notebook and normalizes the merged notebook.
        """
        merged = nbformat.v4.new_notebook()
        for notebook_path in notebooks:
            nb = self.validator.validate_and_add_ids(notebook_path)
            merged.cells.extend(nb.cells)

        return merged
