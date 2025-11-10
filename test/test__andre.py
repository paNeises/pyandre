import pytest


import andre


def test_validate_arid_list_unique_ids_1():
    """
    Test validate_arid_list_unique_ids with a list containing only unique
    entries.
    """
    arid_list = ["1", "2", "3"]
    result = andre.validate_arid_list_unique_ids(arid_list)
    assert result is True


def test_validate_arid_list_unique_ids_2():
    """
    Test validate_arid_list_unique_ids with a list containing a duplicate
    entry.
    """
    arid_list = ["1", "2", "3", "3"]
    result = andre.validate_arid_list_unique_ids(arid_list)
    assert result is False


def test_Author_1():
    """
    Test the creation of an Author object with a list containing only unique
    authorship record entries.
    """
    arid_list = ["1", "2", "3"]
    andre.Author(arid_list)
    assert True is True


def test_Author_2():
    """
    Test the creation of an Author object with a list containing duplicate
    authorship record entries.
    """
    arid_list = ["1", "2", "3", "3"]
    with pytest.raises(Exception) as exception:
        andre.Author(arid_list)
    assert exception.type == ValueError
