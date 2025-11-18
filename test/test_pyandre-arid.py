import pytest


from pyandre.arid import Arid


def test_constructur_1():
    """
    Test the constructor of the Arid class witb a valid parameter type.
    """
    Arid("test")


def test_constructur_2():
    """
    Test the constructor of the Arid class with an invalid parameter type.
    """
    with pytest.raises(Exception) as exception:
        Arid(2)
    assert exception.type == TypeError


def test_get_identifier_1():
    """
    Test the get_identifier function of the Arid class.
    """
    arid = Arid("test")
    assert arid.get_identifier() == "test"


def test_check_arid_list_contains_only_unique_arids_1():
    """
    Test the static check_arid_list_contains_only_unique_arids function of the
    Arid class with a list containing only unique Arid's.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_list = [arid_1, arid_2]
    assert Arid.check_arid_list_contains_only_unique_arids(arid_list) is True


def test_check_arid_list_contains_only_unique_arids_2():
    """
    Test the static check_arid_list_contains_only_unique_arids function of the
    Arid class with a list containing a duplicate Arid's.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("1")
    arid_list = [arid_1, arid_2, arid_3]
    assert Arid.check_arid_list_contains_only_unique_arids(arid_list) is False


def test_arid_list_to_arid_identifier_list_1():
    """
    Test the static arid_list_to_arid_identifier_list function of the
    Arid class.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_list = [arid_1, arid_2]
    identifier_list = ["1", "2"]
    assert Arid.arid_list_to_arid_identifier_list(arid_list) == identifier_list
