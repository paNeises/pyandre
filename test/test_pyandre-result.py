import math


import pytest


from pyandre.result import Arid, Cluster, Result


def test_constructor_1():
    """
    Test the creation of a Result object with valid cluster lists.
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
    Test the creation of a Result object with valid cluster lists where
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
    Test the creation of a Result object with invalid cluster lists, where
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
    Test the creation of a Result object with invalid cluster lists, where
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
    Test the creation of a Result object with invalid cluster lists, where
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
    Test the creation of a Result object with invalid cluster lists, where
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


def test_constructor_7():
    """
    Test the creation of a Result object with invalid cluster lists, where
    the theoretical one contains an object that is not a pyandre.Cluster
    object.
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
    theoretical_clusters = [cluster_1, cluster_2, "1"]
    empirical_clusters = [cluster_3, cluster_4, cluster_5]
    with pytest.raises(Exception) as exception:
        Result(theoretical_clusters, empirical_clusters)
    assert exception.type == TypeError


def test_constructor_8():
    """
    Test the creation of a Result object with invalid cluster lists, where
    the empirical one contains an object that is not a pyandre.Cluster object.
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
    empirical_clusters = [cluster_3, cluster_4, cluster_5, "1"]
    with pytest.raises(Exception) as exception:
        Result(theoretical_clusters, empirical_clusters)
    assert exception.type == TypeError


def test_get_contained_arids():
    """
    Test the get_contained_arids function of the Result class.
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


def test_compute_average_cluster_purity_1():
    """
    Test the compute_average_cluster_purity function from the Result
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


def test_compute_average_author_purity_1():
    """
    Test the compute_average_author_purity function from a Result object.
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


def test_compute_k_1():
    """
    Test the compute_k function from a Result object.
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


def test_compute_pairwise_precision_1():
    """
    Test the compute_pairwise_precision function from a Result object.
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
    pp = 6 / 7
    assert result.compute_pairwise_precision() == pp


def test_compute_pairwise_precision_2():
    """
    Test the compute_pairwise_precision function from a Result object when
    pairwise precision is undefined.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_list_cluster_1 = [arid_1, arid_2, arid_3]
    arid_list_cluster_2 = [arid_1]
    arid_list_cluster_3 = [arid_2]
    arid_list_cluster_4 = [arid_3]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    theoretical_clusters = [cluster_1]
    empirical_clusters = [cluster_2, cluster_3, cluster_4]
    result = Result(theoretical_clusters, empirical_clusters)
    assert result.compute_pairwise_precision() is None


def test_compute_pairwise_recall_1():
    """
    Test the compute_pairwise_recall function from a Result object.
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
    pr = 6 / 10
    assert result.compute_pairwise_recall() == pr


def test_compute_pairwise_recall_2():
    """
    Test the compute_pairwise_recall function from a Result object when
    pairwise recall is undefined.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_list_cluster_1 = [arid_1]
    arid_list_cluster_2 = [arid_2]
    arid_list_cluster_3 = [arid_3]
    arid_list_cluster_4 = [arid_1, arid_2, arid_3]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    theoretical_clusters = [cluster_1, cluster_2, cluster_3]
    empirical_clusters = [cluster_4]
    result = Result(theoretical_clusters, empirical_clusters)
    assert result.compute_pairwise_recall() is None


def test_compute_pairwise_f1_1():
    """
    Test the compute_pairwise_f1 function from a Result object.
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
    pp = 6 / 7
    pr = 6 / 10
    pf1 = (2 * pp * pr) / (pp + pr)
    assert result.compute_pairwise_f1() == pf1


def test_compute_pairwise_f1_2():
    """
    Test the compute_pairwise_f1 function from a Result object when pairwise
    precision is undefined.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_list_cluster_1 = [arid_1, arid_2, arid_3]
    arid_list_cluster_2 = [arid_1]
    arid_list_cluster_3 = [arid_2]
    arid_list_cluster_4 = [arid_3]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    theoretical_clusters = [cluster_1]
    empirical_clusters = [cluster_2, cluster_3, cluster_4]
    result = Result(theoretical_clusters, empirical_clusters)
    assert result.compute_pairwise_f1() is None


def test_compute_pairwise_f1_3():
    """
    Test the compute_pairwise_f1 function from a Result object when pairwise
    recall is undefined.
    """
    arid_1 = Arid("1")
    arid_2 = Arid("2")
    arid_3 = Arid("3")
    arid_list_cluster_1 = [arid_1]
    arid_list_cluster_2 = [arid_2]
    arid_list_cluster_3 = [arid_3]
    arid_list_cluster_4 = [arid_1, arid_2, arid_3]
    cluster_1 = Cluster(arid_list_cluster_1)
    cluster_2 = Cluster(arid_list_cluster_2)
    cluster_3 = Cluster(arid_list_cluster_3)
    cluster_4 = Cluster(arid_list_cluster_4)
    theoretical_clusters = [cluster_1, cluster_2, cluster_3]
    empirical_clusters = [cluster_4]
    result = Result(theoretical_clusters, empirical_clusters)
    assert result.compute_pairwise_f1() is None


def test_compute_cluster_precision_1():
    """
    Test the compute_cluster_precision function from a Result object.
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
    cp = 1 / 4
    assert result.compute_cluster_precision() == cp


def test_compute_cluster_recall_1():
    """
    Test the compute_cluster_recall function from a Result object.
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
    cr = 1 / 3
    assert result.compute_cluster_recall() == cr


def test_compute_cluster_f1_1():
    """
    Test the compute_cluster_f1 function from a Result object.
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
    cp = 1 / 4
    cr = 1 / 3
    cf1 = (2 * cp * cr) / (cp + cr)
    assert result.compute_cluster_f1() == cf1


def test_compute_ratio_of_cluster_size_1():
    """
    Test the compute_ratio_of_cluster_size function from the Result
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
    rcs = 4 / 3
    assert result.compute_ratio_of_cluster_size() == rcs


def test_compute_bp_1():
    """
    Test the compute_ratio_of_cluster_size function from the Result
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
    bp = 8 / 9
    assert result.compute_bp() == bp


def test_compute_br_1():
    """
    Test the compute_ratio_of_cluster_size function from the Result
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
    br = (1 / 9) * (3 / 4) + (1 / 9) * (3 / 4) + (1 / 9) * (3 / 4) + (1 / 9)\
        * (1 / 4) + (1 / 9) * (3 / 3) + (1 / 9) * (3 / 3) + (1 / 9)\
        * (3 / 3) + (1 / 9) * (1 / 2) + (1 / 9) * (1 / 2)
    assert result.compute_br() == br


def test_compute_bFa_1():
    """
    Test the compute_ratio_of_cluster_size function from the Result
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
    bp = 8 / 9
    br = (1 / 9) * (3 / 4) + (1 / 9) * (3 / 4) + (1 / 9) * (3 / 4) + (1 / 9)\
        * (1 / 4) + (1 / 9) * (3 / 3) + (1 / 9) * (3 / 3) + (1 / 9)\
        * (3 / 3) + (1 / 9) * (1 / 2) + (1 / 9) * (1 / 2)
    bfa = 1 / ((0.5 / bp) + (0.5 / br))
    assert result.compute_bFa() == bfa
