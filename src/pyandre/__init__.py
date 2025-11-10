class Author():
    """
    A class for representing an author as the list of its authorship record
    ID's.
    """

    def __init__(self, arid_list: list[str]):
        """
        Checks if the provided list of authorship record ID's contains only
        unique entries and then creates and Author object with this list of
        authorship record ID's. If the provided list contains duplicates,
        an exception is raised.

        Keyword arguments:
        arid_list: The list of authorship record ID's that belog to the author.
        """
        if not validate_arid_list_unique_arids(arid_list):
            raise ValueError("The given arid_list contains duplicate entries, "
                             "but creating an Author object with duplicates "
                             "in the arid_list is forbidden.")
        self._arid_list: list[str] = arid_list

    def get_arid_list(self) -> list[str]:
        """
        Get the list of authorship records that belong to this author.
        """
        return self._arid_list


class BlockResult():
    """
    A class for representing the results of an author name disambiguation
    system of a block (obtained by a blocking procedure) of authorship records.
    The class conatins 2 lists of Author objects, one indicating the correct
    disambiguation result and the other indicating the results obtained by the
    system that should be evaluated.
    """

    def __init__(self,
                 correct_authors: list[Author],
                 obtained_authors: list[Author]):
        """
        Checks that both author lists are valid in the sence that the authors
        in each list do not share an authorship record and checks if both lists
        cover the same authorship records. If both checks succeed, a
        BlockResult object is created. If a check failes, an exception is
        raised.

        Keyword arguments:
        correct_authors: The list of correctly disambiguated authors.
        obtained_authors: The list of authors obtained from the system that
        should be evaluated.
        """
        correct_authors_arids: list[str] =\
            get_arids_from_author_list(correct_authors)
        obtained_authors_arids: list[str] =\
            get_arids_from_author_list(obtained_authors)
        if not validate_arid_list_unique_arids(correct_authors_arids):
            raise ValueError("The given correct authors list contains authors "
                             "that share an authorship, which is forbidden "
                             "when creating BlockResult object.")
        if not validate_arid_list_unique_arids(obtained_authors_arids):
            raise ValueError("The given obtained authors list contains "
                             "authors that share an authorship, which is "
                             "forbidden when creating BlockResult object.")
        if set(correct_authors_arids) != set(obtained_authors_arids):
            raise ValueError("The set of authorship records accumulated over "
                             "all authors in the correct_authors list is not "
                             "equal to the set of authorship records "
                             "accumulated over all author in the "
                             "obtained_authors list, which is forbidden when "
                             "creating a BlockResult object.")
        self._correct_authors: list[Author] = correct_authors
        self._obtained_authors: list[Author] = obtained_authors
        self._contained_arids: list[str] = correct_authors_arids

    def get_contained_arids(self) -> list[str]:
        """
        Get all authorship record ID's that are contained in the block.
        """
        return self._contained_arids


class BlockCollection():
    """
    A class for representing a collection of blocks obtained by a blocking
    strategy over a author name disambiguation dataset. It requires the
    blocking strategy to produce disjoint blocks, this is checked when
    initializing an object of this class. It contains a list of BlockResult
    objects.
    """

    def __init__(self, block_result_list: list[BlockResult]):
        """
        Checks that the BlockResult objects in the given list do not have a
        common authorship record and the creates a BlockCollection object based
        on the given list. If the check fails, an exception is raised.
        """
        contained_arids = get_arids_from_block_result_list(block_result_list)
        if len(set(contained_arids)) != len(contained_arids):
            raise ValueError("The given list of block results contains at "
                             "least 2 blocks that have a common authorship "
                             "record, whcih is forbidden when creating a "
                             "BlockCollection object.")
        self._block_result_list = block_result_list


def validate_arid_list_unique_arids(arid_list: list[str]) -> bool:
    """
    Validate if a given authorship record ID list contains only unique entries.
    Returns True if the entries are unique, False otherwise.

    Keyword arguments:
    arid_list: The list of authorship record ID's that should be validated.
    """
    arid_set: set[str] = set()
    for arid in arid_list:
        arid_set.add(arid)
    if len(arid_list) == len(arid_set):
        return True
    return False


def get_arids_from_author_list(author_list: list[Author]) -> list[str]:
    """
    Get the list of all authorship records from a list of Author objects. This
    does not check if the resulting list conatins duplicates, which would
    imply that the same authorship record is present in different authors
    in the list.

    Keyword arguments:
    author_list: The list of Author objects.
    """
    arid_list: list[str] = []
    for author in author_list:
        arid_list += author.get_arid_list()
    return arid_list


def get_arids_from_block_result_list(block_result_list: list[BlockResult])\
        -> list[str]:
    """
    Get the list of all authorship records from a list of BlockResult objects.
    This does not check if the resulting list contains duplicates, which would
    imply that the same authorship record is contained in multiple blocks in
    the list.

    Keyword arguments:
    block_result_list: The list of BlockResult objects.
    """
    arid_list: list[str] = []
    for block_result in block_result_list:
        arid_list += block_result.get_contained_arids()
    return arid_list
