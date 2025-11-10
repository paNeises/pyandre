def validate_arid_list_unique_ids(arid_list):
    """
    Validate if a given authorship record ID list contains only unique entries.
    Returns True if the entries are unique, False otherwise.

    Keyword arguments:
    arid_list: The list of authorship record ID's that should be validated.
    """

    arid_set = set()
    for arid in arid_list:
        arid_set.add(arid)
    if len(arid_list) == len(arid_set):
        return True
    return False


class Author():
    """
    A class for representing an author as the list of its authorship record
    ID's.
    """

    def __init__(self, arid_list):
        """
        Checks if the provided list of authorship record ID's contains only
        unique entries and then creates and Author object with this list of
        authorship record ID's. If the provided list contains duplicates,
        an exception is thrown.

        Keyword arguments:
        arid_list: The list of authorship record ID's that belog to the author.
        """
        if not validate_arid_list_unique_ids(arid_list):
            raise ValueError("The given arid_list contains duplicate entries, "
                             "but creating an author with duplicates in the "
                             "arid_list is forbidden.")
        self._arid_list = arid_list
