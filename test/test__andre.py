import pytest


import andre


def test_Author_1():
    """
    Test the creation of an Author object with a list containing only unique
    authorship record entries.
    """
    arid_list = ["1", "2", "3"]
    andre.Author(arid_list)


def test_Author_2():
    """
    Test the creation of an Author object with a list containing duplicate
    authorship record entries.
    """
    arid_list = ["1", "2", "3", "3"]
    with pytest.raises(Exception) as exception:
        andre.Author(arid_list)
    assert exception.type == ValueError


def test_Author_get_arid_list_1():
    """
    Test the get_arid_list function of an Author object.
    """
    arid_list = ["1", "2", "3"]
    author = andre.Author(arid_list)
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
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_3 = andre.Author(arid_list_author_3)
    author_4 = andre.Author(arid_list_author_4)
    author_5 = andre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    andre.BlockResult(correct_authors, obtained_authors)


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
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_3 = andre.Author(arid_list_author_3)
    author_4 = andre.Author(arid_list_author_4)
    author_5 = andre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        andre.BlockResult(correct_authors, obtained_authors)
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
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_3 = andre.Author(arid_list_author_3)
    author_4 = andre.Author(arid_list_author_4)
    author_5 = andre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        andre.BlockResult(correct_authors, obtained_authors)
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
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_3 = andre.Author(arid_list_author_3)
    author_4 = andre.Author(arid_list_author_4)
    author_5 = andre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        andre.BlockResult(correct_authors, obtained_authors)
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
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_3 = andre.Author(arid_list_author_3)
    author_4 = andre.Author(arid_list_author_4)
    author_5 = andre.Author(arid_list_author_5)
    correct_authors = [author_1, author_2]
    obtained_authors = [author_3, author_4, author_5]
    with pytest.raises(Exception) as exception:
        andre.BlockResult(correct_authors, obtained_authors)
    assert exception.type == ValueError


def test_validate_arid_list_unique_arids_1():
    """
    Test validate_arid_list_unique_ids with a list containing only unique
    entries.
    """
    arid_list = ["1", "2", "3"]
    result = andre.validate_arid_list_unique_arids(arid_list)
    assert result is True


def test_validate_arid_list_unique_arids_2():
    """
    Test validate_arid_list_unique_ids with a list containing a duplicate
    entry.
    """
    arid_list = ["1", "2", "3", "3"]
    result = andre.validate_arid_list_unique_arids(arid_list)
    assert result is False


def test_get_arids_from_author_list_1():
    """
    Test get_arids_from_author_list with two authors that do not share an
    authorship record.
    """
    arid_list_author_1 = ["1", "2", "5"]
    arid_list_author_2 = ["3", "4"]
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_list = [author_1, author_2]
    result = andre.get_arids_from_author_list(author_list)
    assert result == ["1", "2", "5", "3", "4"]


def test_get_arids_from_author_list_2():
    """
    Test get_arids_from_author_list with two authors that share an authorship
    record.
    """
    arid_list_author_1 = ["1", "2", "3"]
    arid_list_author_2 = ["3", "4"]
    author_1 = andre.Author(arid_list_author_1)
    author_2 = andre.Author(arid_list_author_2)
    author_list = [author_1, author_2]
    result = andre.get_arids_from_author_list(author_list)
    assert result == ["1", "2", "3", "3", "4"]
