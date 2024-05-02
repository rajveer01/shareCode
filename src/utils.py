class Cleaners:
    """
    A collection of static methods for cleaning and processing strings.

    Methods
    -------
    stripper(value: str) -> str:
        Remove leading and trailing whitespaces from a string.

    lister(value: str) -> list[str]:
        Split a string into a list of substrings based on whitespace.

    """

    @staticmethod
    def stripper(value: str) -> str:
        """
        Remove leading and trailing whitespaces from a string.

        Parameters
        ----------
        value : str
            The input string to be stripped.

        Returns
        -------
        str
            The input string after stripping leading and trailing whitespaces.
        """
        return value.strip()

    @staticmethod
    def lister(value: str) -> list[str]:
        """
        Split a string into a list of substrings based on whitespace.

        Parameters
        ----------
        value : str
            The input string to be split.

        Returns
        -------
        list[str]
            A list of substrings obtained by splitting the input string based on whitespace.

        """
        return value.split()
