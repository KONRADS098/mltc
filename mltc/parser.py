import click


class IndexParser:
    def __init__(self, indices_str):
        self.indices_str = indices_str

    def parse_indices(self):
        """
        Parse and validate user input for notebook indices.
        Returns a list of valid indices.
        """
        indices = self.indices_str.split()
        valid_indices = []
        for index in indices:
            try:
                idx = int(index) - 1  # convert to 0-based index
                if idx >= 0:
                    valid_indices.append(idx)
                else:
                    click.echo(
                        f"Index {index} is out of range. Indices must be positive integers."
                    )
            except ValueError:
                click.echo(f"Invalid input '{index}': Please enter only integers.")
                return []

        return valid_indices
