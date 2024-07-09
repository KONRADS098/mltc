class InvalidIndexError(Exception):
    """Exception raised for invalid index values."""

    def __init__(self, index: int) -> None:
        """Initialize the Parser object.

        Args:
            index (int): The index value for the Parser object.

        Raises:
        ValueError: If the index is out of range. Indices must be positive integers.
        """
        self.index = index
        super().__init__(f"Index {index} is out of range. Indices must be positive integers.")


class InvalidInputError(Exception):
    """Exception raised for invalid input values."""

    def __init__(self, input_value: any) -> None:
        """Initializes the InvalidInputError class with an input value.

        Args:
            input_value: The invalid input value that caused the exception.
        """
        self.input_value = input_value
        super().__init__(f"Invalid input '{input_value}': Please enter only integers.")


class IndexParser:
    """Parses and validates a string of space-separated indices.

    This class is designed to take a string of space-separated indices, typically provided by user input,
    and convert it into a list of integer indices. It ensures that all indices are valid positive integers
    and converts them to a 0-based indexing system used in programming.

    Attributes:
        indices (str): A string containing space-separated indices intended for parsing.
    """

    def __init__(self, indices: str) -> None:
        """Initializes the IndexParser with a string of indices.

        Args:
            indices (str): A string of space-separated indices. Each index should represent an integer.
                           The indices are expected to be 1-based and will be converted to 0-based indices.
        """
        self.indices = indices

    def parse_indices(self) -> list[int]:
        """Parses the provided indices string into a list of 0-based integer indices.

        This method splits the input string into individual indices, attempts to convert each to an integer,
        and adjusts them to 0-based indexing. It validates that each index is a positive integer. If any index
        is invalid (not a positive integer), an InvalidInputError is raised. Likewise, if the index is out of range,
        an InvalidIndexError is raised.

        Returns:
            list[int]: A list of valid 0-based integer indices. If any index is invalid, returns an empty list.
        """
        indices = self.indices.split()
        valid_indices = []
        for index in indices:
            try:
                idx = int(index) - 1  # convert to 0-based index
                if idx >= 0:
                    valid_indices.append(idx)
                else:
                    raise InvalidIndexError(index)
            except ValueError as err:
                raise InvalidInputError(index) from err

        return valid_indices
