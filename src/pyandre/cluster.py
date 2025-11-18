from pyandre.arid import Arid


class Cluster():
    """
    A class for representing a cluster of authorship record ID's (Arid's).
    """

    def __init__(self, arid_list: list[Arid]):
        """
        Creates a Cluster object based on a list of given authorship records.
        The type of the object in the list is checked as well as that the
        Arid's all have unique identifiers.

        Keyword arguments:
        arid_list: The list of authorship record ID's.
        """
        if len(arid_list) == 0:
            raise ValueError("The Arid list contains no elements, which is "
                             "forbidden when creating a Cluster object")
        for arid in arid_list:
            if not isinstance(arid, Arid):
                raise TypeError("The Arid list contains an item that is not "
                                "an Arid.")
        if not Arid.check_arid_list_contains_only_unique_arids(arid_list):
            raise ValueError("The given Arid list contains duplicate "
                             "identifiers, which is forbidden when creating a "
                             "Cluster object.")
        self._arid_list: list[Arid] = arid_list

    def get_arid_list(self) -> list[Arid]:
        """
        Get the list of authorship records that belong to this author.
        """
        return self._arid_list
