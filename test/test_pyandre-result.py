import math


import pytest


from pyandre.result import Arid, Cluster, Result


def test_constructor_1():
    """
    Test the creation of a BlockResult object with valid cluster lists.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_list_cluster_1 = [arid_1, arid_2]
    arid_list_cluster_2 = [arid_3, arid_4]
    arid_list_cluster_3 = [arid_1]
    arid_list_cluster_4 = [arid_2, arid_3]
    arid_list_cluster_5 = [arid_4]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    Result(theoretical_clusters, empirical_clusters)


def test_constructor_2():
    """
    Test the creation of a BlockResult object with valid cluster lists where
    distinct Arid objects are used in the theoretical and the empirical
    clusters for the same arid identifier.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("1")
    arid_6 = Arid("2")
    arid_7 = Arid("3")
    arid_8 = Arid("4")
    arid_list_cluster_1 = [arid_1, arid_2]
    arid_list_cluster_2 = [arid_3, arid_4]
    arid_list_cluster_3 = [arid_5]
    arid_list_cluster_4 = [arid_6, arid_7]
    arid_list_cluster_5 = [arid_8]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    Result(theoretical_clusters, empirical_clusters)


def test_constructor_3():
    """
    Test the creation of a BlockResult object with invalid cluster lists, where
    the theoretical one contains duplicate authorship records between its
    clusters.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("3")
    arid_list_cluster_1 = [arid_1, arid_2, arid_5]
    arid_list_cluster_2 = [arid_3, arid_4]
    arid_list_cluster_3 = [arid_1]
    arid_list_cluster_4 = [arid_2, arid_3]
    arid_list_cluster_5 = [arid_4]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    with pytest.raises(Exception) as exception:
        Result(theoretical_clusters, empirical_clusters)
    assert exception.type == ValueError


def test_constructor_4():
    """
    Test the creation of a BlockResult object with invalid cluster lists, where
    the empirical one contains duplicate authorship records between its
    clusters.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("3")
    arid_list_cluster_1 = [arid_1, arid_2]
    arid_list_cluster_2 = [arid_3, arid_4]
    arid_list_cluster_3 = [arid_1, arid_5]
    arid_list_cluster_4 = [arid_2, arid_3]
    arid_list_cluster_5 = [arid_4]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    with pytest.raises(Exception) as exception:
        Result(theoretical_clusters, empirical_clusters)
    assert exception.type == ValueError


def test_constructor_5():
    """
    Test the creation of a BlockResult object with invalid cluster lists, where
    the theoretical one contains one authorship record not presend in the
    empirical one.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("5")
    arid_list_cluster_1 = [arid_1, arid_2]
    arid_list_cluster_2 = [arid_3, arid_4, arid_5]
    arid_list_cluster_3 = [arid_1]
    arid_list_cluster_4 = [arid_2, arid_3]
    arid_list_cluster_5 = [arid_4]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    with pytest.raises(Exception) as exception:
        Result(theoretical_clusters, empirical_clusters)
    assert exception.type == ValueError


def test_constructor_6():
    """
    Test the creation of a BlockResult object with invalid cluster lists, where
    the empirical one contains one authorship record not presend in the
    theoretical one.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("5")
    arid_list_cluster_1 = [arid_1, arid_2]
    arid_list_cluster_2 = [arid_3, arid_4]
    arid_list_cluster_3 = [arid_1]
    arid_list_cluster_4 = [arid_2, arid_3]
    arid_list_cluster_5 = [arid_4, arid_5]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    with pytest.raises(Exception) as exception:
        Result(theoretical_clusters, empirical_clusters)
    assert exception.type == ValueError


def test_get_contained_arids():
    """
    Test the get_contained_arids function of the BlockResult class.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_list_cluster_1 = [arid_1, arid_2]
    arid_list_cluster_2 = [arid_3, arid_4]
    arid_list_cluster_3 = [arid_1]
    arid_list_cluster_4 = [arid_2, arid_3]
    arid_list_cluster_5 = [arid_4]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    theoretical_clusters = [cluster_1, cluster_2]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    result = Result(theoretical_clusters, empirical_clusters)
    all_arids = [arid_1, arid_2, arid_3, arid_4]
    assert result.get_contained_arids() == all_arids


def test_BlockResult_compute_average_cluster_purity_1():
    """
    Test the compute_average_cluster_purity function from the BlockResult
    class.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("5")
    arid_6 = Arid("6")
    arid_7 = Arid("7")
    arid_8 = Arid("8")
    arid_9 = Arid("9")
    arid_list_cluster_1 = [arid_1, arid_2, arid_3, arid_4]
    arid_list_cluster_2 = [arid_5, arid_6, arid_7]
    arid_list_cluster_3 = [arid_8, arid_9]
    arid_list_cluster_4 = [arid_1, arid_2, arid_3]
    arid_list_cluster_5 = [arid_5, arid_6, arid_7]
    arid_list_cluster_6 = [arid_4, arid_8]
    arid_list_cluster_7 = [arid_9]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    cluster_6 = Cluster(arid_list_cluster_6)
    cluster_7 = Cluster(arid_list_cluster_7)
    theoretical_clusters = [cluster_1, cluster_2, cluster_3]
    empirical_clusters = [cluster_4, cluster_5, cluster_6, cluster_7]
    result = Result(theoretical_clusters, empirical_clusters)
    acp = 8 / 9
    assert result.compute_average_cluster_purity() == acp


def test_BlockResult_compute_average_author_purity_1():
    """
    Test the compute_average_author_purity function from a BlockResult object.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("5")
    arid_6 = Arid("6")
    arid_7 = Arid("7")
    arid_8 = Arid("8")
    arid_9 = Arid("9")
    arid_list_cluster_1 = [arid_1, arid_2, arid_3, arid_4]
    arid_list_cluster_2 = [arid_5, arid_6, arid_7]
    arid_list_cluster_3 = [arid_8, arid_9]
    arid_list_cluster_4 = [arid_1, arid_2, arid_3]
    arid_list_cluster_5 = [arid_5, arid_6, arid_7]
    arid_list_cluster_6 = [arid_4, arid_8]
    arid_list_cluster_7 = [arid_9]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    cluster_6 = Cluster(arid_list_cluster_6)
    cluster_7 = Cluster(arid_list_cluster_7)
    theoretical_clusters = [cluster_1, cluster_2, cluster_3]
    empirical_clusters = [cluster_4, cluster_5, cluster_6, cluster_7]
    result = Result(theoretical_clusters, empirical_clusters)
    aap = 6.5 / 9
    assert result.compute_average_author_purity() == aap


def test_BlockResult_compute_k_1():
    """
    Test the compute_k function from a BlockResult object.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_4 = Arid("4")
    arid_5 = Arid("5")
    arid_6 = Arid("6")
    arid_7 = Arid("7")
    arid_8 = Arid("8")
    arid_9 = Arid("9")
    arid_list_cluster_1 = [arid_1, arid_2, arid_3, arid_4]
    arid_list_cluster_2 = [arid_5, arid_6, arid_7]
    arid_list_cluster_3 = [arid_8, arid_9]
    arid_list_cluster_4 = [arid_1, arid_2, arid_3]
    arid_list_cluster_5 = [arid_5, arid_6, arid_7]
    arid_list_cluster_6 = [arid_4, arid_8]
    arid_list_cluster_7 = [arid_9]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    cluster_5 = Cluster(arid_list_cluster_5)
    cluster_6 = Cluster(arid_list_cluster_6)
    cluster_7 = Cluster(arid_list_cluster_7)
    theoretical_clusters = [cluster_1, cluster_2, cluster_3]
    empirical_clusters = [cluster_4, cluster_5, cluster_6, cluster_7]
    result = Result(theoretical_clusters, empirical_clusters)
    k = math.sqrt((8 / 9) * (6.5 / 9))
    assert result.compute_k() == k
