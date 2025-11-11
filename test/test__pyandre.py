import pytest


import pyandre


def test_Author_1():
    """
    Test the creation of an Author object with a list containing only unique
    authorship record entries.
    """
    arid_list = ["1", "2", "3"]
    pyandre.Author(arid_list)


def test_Author_2():
    """
    Test the creation of an Author object with a list containing duplicate
    authorship record entries.
    """
    arid_list = ["1", "2", "3", "3"]
    with pytest.raises(Exception) as exception:
        pyandre.Author(arid_list)
    assert exception.type == ValueError


def test_Author_get_arid_list_1():
    """
    Test the get_arid_list function of an Author object.
    """
    arid_list = ["1", "2", "3"]
    author = pyandre.Author(arid_list)
    author_arid_list = author.get_arid_list()
    assert arid_list == author_arid_list


def test_BlockResult_1():
    """
    Test the creation of a BlockResult object with valid author lists.
    """
    arid_list_author_1 = ["1", "2"]
    arid_list_author_2 = ["3", "4"]
    arid_list_author_3 = ["1"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    pyandre.BlockResult(correct_authors, obtained_authors)


def test_BlockResult_2():
    """
    Test the creation of a BlockResult object with invalid author lists, where
    the correct one contains duplicate authorship records between ist authors.
    """
    arid_list_author_1 = ["1", "2", "3"]
    arid_list_author_2 = ["3", "4"]
    arid_list_author_3 = ["1"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        pyandre.BlockResult(correct_authors, obtained_authors)
    assert exception.type == ValueError


def test_BlockResult_3():
    """
    Test the creation of a BlockResult object with invalid author lists, where
    the obtained one contains duplicate authorship records between ist authors.
    """
    arid_list_author_1 = ["1", "2"]
    arid_list_author_2 = ["3", "4"]
    arid_list_author_3 = ["1", "2"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        pyandre.BlockResult(correct_authors, obtained_authors)
    assert exception.type == ValueError


def test_BlockResult_4():
    """
    Test the creation of a BlockResult object with invalid author lists, where
    the correct one contains one authorship record not presend in the obtained
    one.
    """
    arid_list_author_1 = ["1", "2"]
    arid_list_author_2 = ["3", "4", "5"]
    arid_list_author_3 = ["1"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        pyandre.BlockResult(correct_authors, obtained_authors)
    assert exception.type == ValueError


def test_BlockResult_5():
    """
    Test the creation of a BlockResult object with invalid author lists, where
    the obtained one contains one authorship record not presend in the correct
    one.
    """
    arid_list_author_1 = ["1", "2"]
    arid_list_author_2 = ["3", "4"]
    arid_list_author_3 = ["1"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4", "5"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        pyandre.BlockResult(correct_authors, obtained_authors)
    assert exception.type == ValueError


def test_BlockResult_get_correct_authors_1():
    """
    Test the get_correct_authors function of the BlockResult class.
    """
    arid_list_author_1 = ["1", "2"]
    arid_list_author_2 = ["3", "4"]
    arid_list_author_3 = ["1"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    block_result = pyandre.BlockResult(correct_authors, obtained_authors)
    result = block_result.get_correct_authors()
    assert correct_authors == result


def test_BlockResult_get_obtained_authors_1():
    """
    Test the get_obtained_authors function of the BlockResult class.
    """
    arid_list_author_1 = ["1", "2"]
    arid_list_author_2 = ["3", "4"]
    arid_list_author_3 = ["1"]
    arid_list_author_4 = ["2", "3"]
    arid_list_author_5 = ["4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    block_result = pyandre.BlockResult(correct_authors, obtained_authors)
    result = block_result.get_obtained_authors()
    assert obtained_authors == result


def test_BlockResult_get_contained_arids_1():
    """
    Test the get_contained_arids function from a BlockResult object.
    """
    arid_list_author_1 = ["1", "3"]
    arid_list_author_2 = ["2", "4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_list = [author_1, author_2]
    blockresult = pyandre.BlockResult(author_list, author_list)
    result = blockresult.get_contained_arids()
    assert result == ["1", "3", "2", "4"]


def test_BlockResult_compute_average_cluster_purity_1():
    arid_list_author_1 = ["1", "2", "3", "4"]
    arid_list_author_2 = ["5", "6", "7"]
    arid_list_author_3 = ["8", "9"]
    arid_list_author_4 = ["1", "2", "3"]
    arid_list_author_5 = ["5", "6", "7"]
    arid_list_author_6 = ["4", "8"]
    arid_list_author_7 = ["9"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_4 = pyandre.Author(arid_list_author_4)
    author_5 = pyandre.Author(arid_list_author_5)
    author_6 = pyandre.Author(arid_list_author_6)
    author_7 = pyandre.Author(arid_list_author_7)
    correct_authors = [author_1, author_2, author_3]
    obtained_authors = [author_4, author_5, author_6, author_7]
    block_result = pyandre.BlockResult(correct_authors, obtained_authors)
    acp = 8 / 9
    result = block_result.compute_average_cluster_purity()
    assert result == acp


def test_BlockCollection_1():
    """
    Test the creation of a BlockCollection object with a valid
    block_result_list.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    pyandre.BlockCollection(block_result_list)


def test_BlockCollection_2():
    """
    Test the creation of a BlockCollection object with a block_result_list that
    contains blocks which share an authorship record.
    """
    arid_list_author_1 = ["1", "2", "5", "6"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    with pytest.raises(Exception) as exception:
        pyandre.BlockCollection(block_result_list)
    assert exception.type == ValueError


def test_BlockCollection_get_correct_authors_1():
    """
    Test the get_correct_authors function of the BlockCollection class.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    block_collection = pyandre.BlockCollection(block_result_list)
    full_author_list = [author_1, author_2, author_3]
    result = block_collection.get_correct_authors()
    assert result == full_author_list


def test_BlockCollection_get_obtained_authors_1():
    """
    Test the get_obtained_authors function of the BlockCollection class.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    block_collection = pyandre.BlockCollection(block_result_list)
    full_author_list = [author_1, author_2, author_3]
    result = block_collection.get_obtained_authors()
    assert result == full_author_list


def test_BlockCollection_get_contained_arids_1():
    """
    Test the get_contained_arids function of the BlockCollection class.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    block_collection = pyandre.BlockCollection(block_result_list)
    full_arid_list = ["1", "2", "5", "3", "4", "8", "6", "7"]
    result = block_collection.get_contained_arids()
    assert result == full_arid_list


def test_validate_arid_list_unique_arids_1():
    """
    Test validate_arid_list_unique_ids with a list containing only unique
    entries.
    """
    arid_list = ["1", "2", "3"]
    result = pyandre.validate_arid_list_unique_arids(arid_list)
    assert result is True


def test_validate_arid_list_unique_arids_2():
    """
    Test validate_arid_list_unique_ids with a list containing a duplicate
    entry.
    """
    arid_list = ["1", "2", "3", "3"]
    result = pyandre.validate_arid_list_unique_arids(arid_list)
    assert result is False


def test_get_arids_from_author_list_1():
    """
    Test get_arids_from_author_list with two authors that do not share an
    authorship record.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_list = [author_1, author_2]
    result = pyandre.get_arids_from_author_list(author_list)
    assert result == ["1", "2", "5", "3", "4"]


def test_get_arids_from_author_list_2():
    """
    Test get_arids_from_author_list with two authors that share an authorship
    record.
    """
    arid_list_author_1 = ["1", "2", "3"]
    arid_list_author_2 = ["3", "4"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_list = [author_1, author_2]
    result = pyandre.get_arids_from_author_list(author_list)
    assert result == ["1", "2", "3", "3", "4"]


def test_get_arids_from_block_result_list_1():
    """
    Test get_arids_from_block_result_list with two blocks which do not contain
    a duplicate authorship record.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    result = pyandre.get_arids_from_block_result_list(block_result_list)
    assert result == ["1", "2", "5", "3", "4", "8", "6", "7"]


def test_get_arids_from_block_result_list_2():
    """
    Test get_arids_from_block_result_list with two blocks which do contain a
    duplicate authorship record.
    """
    arid_list_author_1 = ["1", "2", "5", "6"]
    arid_list_author_2 = ["3", "4", "8"]
    arid_list_author_3 = ["6", "7"]
    author_1 = pyandre.Author(arid_list_author_1)
    author_2 = pyandre.Author(arid_list_author_2)
    author_3 = pyandre.Author(arid_list_author_3)
    author_list_1 = [author_1, author_2]
    author_list_2 = [author_3]
    block_result_1 = pyandre.BlockResult(author_list_1, author_list_1)
    block_result_2 = pyandre.BlockResult(author_list_2, author_list_2)
    block_result_list = [block_result_1, block_result_2]
    result = pyandre.get_arids_from_block_result_list(block_result_list)
    assert result == ["1", "2", "5", "6", "3", "4", "8", "6", "7"]
