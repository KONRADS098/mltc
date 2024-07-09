import uuid
import nbformat


class NotebookValidator:
    @staticmethod
    def add_ids_to_cells(nb):
        """
        Adds a unique 'id' field to each cell in the notebook.
        """
        for cell in nb.cells:
            if "id" not in cell.metadata:
                cell.metadata["id"] = str(uuid.uuid4())  # sssign a new UUID as the ID
        return nb

    @staticmethod
    def validate_and_add_ids(nb_path):
        """
        Validates the notebook and ensures that each cell has a unique 'id' field.
        Throws an error if the notebook cannot be merged.
        """
        with open(nb_path) as f:
            nb = nbformat.read(f, as_version=4)
            nb = NotebookValidator.add_ids_to_cells(
                nb
            )  # ensure all cells have an 'id' field
            try:
                nbformat.validate(nb)
            except nbformat.ValidationError:
                raise RuntimeError(
                    f"The notebook {nb_path} is incapable of merging due to validation errors."
                )
        return nb
