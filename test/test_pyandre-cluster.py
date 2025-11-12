import pytest


from pyandre.cluster import Arid, Cluster


def test_consturctor_1():
    """
    Test the constructor of the Cluster class with a valid list of Arid
    objects.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_list = [arid_1, arid_2]
    Cluster(arid_list)


def test_consturctor_2():
    """
    Test the constructor of the Cluster class with a valid list containing an
    object of the wrong type.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_list = [arid_1, arid_2, 3]
    with pytest.raises(Exception) as exception:
        Cluster(arid_list)
    assert exception.type == TypeError


def test_consturctor_3():
    """
    Test the constructor of the Cluster class with a valid list containing a
    duplicate identifier.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("1")
    arid_list = [arid_1, arid_2, arid_3]
    with pytest.raises(Exception) as exception:
        Cluster(arid_list)
    assert exception.type == ValueError


def test_get_arid_list_1():
    """
    Test the get_arid_list function of the Cluster class.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_list = [arid_1, arid_2]
    cluster = Cluster(arid_list)
    assert cluster.get_arid_list() == arid_list
