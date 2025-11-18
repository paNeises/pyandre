from __future__ import annotations


class Arid():
    """
    A class for representing authorship record ID's.
    """

    def __init__(self, identifier: str):
        """
        Initializes a new Arid with the given identifier string.

        Keyword arguments:
        identifier: The identifier string of the Arid
        """
        if not isinstance(identifier, str):
            raise TypeError("The identifier for an Arid needs to be a string.")
        self._identifier = identifier

    def get_identifier(self):
        """
        Returns the identifier of the Arid object.
        """
        return self._identifier

    def check_arid_list_contains_only_unique_arids(arid_list: list[Arid])\
            -> bool:
        """
        Checks if the identifiers of a given list of Arid's are unique.

        Keyword arguments:
        arid_list: The given list of Arid's.
        """
        arid_id_set: set[str] = set()
        for arid in arid_list:
            arid_id_set.add(arid.get_identifier())
        if len(arid_list) == len(arid_id_set):
            return True
        return False

    def arid_list_to_arid_identifier_list(arid_list: list[Arid]) -> list[str]:
        """
        Takes alist of Arid objects as input and outputs the list of the
        identifiers of these Arid objects.

        Keyword arguments:
        aird_list: The given list of Arid's.
        """
        identifier_list: list[str] = []
        for arid in arid_list:
            identifier_list.append(arid.get_identifier())
        return identifier_list
