import math


from pyandre.arid import Arid
from pyandre.cluster import Cluster


class BlockResult():
    """
    A class for representing the theoretical clusters (the gold standard) and
    the empirical clusters (the results of an author name disambiguation
    system) of a block derived by some blocking procedure.
    """

    def __init__(self,
                 theoretical_clusters: list[Cluster],
                 empirical_clusters: list[Cluster]):
        """
        Create a BlockResult object based on a list of theoretical and a list
        of empirical clusters. Validates for both lists that the union of all
        clusters contains only unique Arid's and that both lists contain the
        same set of arids.
        """
        theoretical_arids: list[Arid] = []
        for cluster in theoretical_clusters:
            theoretical_arids += cluster.get_arid_list()
        if not Arid.check_arid_list_contains_only_unique_arids(
                theoretical_arids):
            raise ValueError("The given theoretical clusters contain "
                             "duplicate Arid's which is forbidden when "
                             "creating a BlockResult object.")
        empirical_arids: list[Arid] = []
        for cluster in empirical_clusters:
            empirical_arids += cluster.get_arid_list()
        if not Arid.check_arid_list_contains_only_unique_arids(
                empirical_arids):
            raise ValueError("The given empirical clusters contain duplicate "
                             "Arid's which is forbidden when creating a "
                             "BlockResult object.")
        theoretical_identifiers = []
        for arid in theoretical_arids:
            theoretical_identifiers.append(arid.get_identifier())
        empirical_identifiers = []
        for arid in empirical_arids:
            empirical_identifiers.append(arid.get_identifier())
        if set(theoretical_identifiers) != set(empirical_identifiers):
            raise ValueError("The set of all Arid's in the theoretical "
                             "clusters does not match the set of all Arid's "
                             "in the empirical clusters, which is forbidden "
                             "when creating a BlockResult object.")
        self._theoretical_clusters: list[Cluster] = theoretical_clusters
        self._empirical_clusters: list[Cluster] = empirical_clusters
        self._contained_arids: list[Arid] = theoretical_arids

    def get_contained_arids(self) -> list[Arid]:
        """
        Get all authorship record IDs that are contained in the block.
        """
        return self._contained_arids

    def compute_average_cluster_purity(self) -> float:
        """
        Compute and return the average cluster purity (ACP) metric of this
        block.
        """
        acp = 0
        for empirical_cluster in self._empirical_clusters:
            for theoretical_cluster in self._theoretical_clusters:
                empirical_arids = empirical_cluster.get_arid_list()
                empirical_arid_set = set()
                for arid in empirical_arids:
                    empirical_arid_set.add(arid.get_identifier())
                theoretical_arids = theoretical_cluster.get_arid_list()
                theoretical_arid_set = set()
                for arid in theoretical_arids:
                    theoretical_arid_set.add(arid.get_identifier())
                n_ij = len(empirical_arid_set & theoretical_arid_set)
                n_i = len(empirical_arid_set)
                acp += n_ij ** 2 / n_i
        n = len(self._contained_arids)
        acp = acp / n
        return acp

    def compute_average_author_purity(self) -> float:
        """
        Compute and return the average author purity (AAP) metric of this
        block.
        """
        aap = 0
        for theoretical_cluster in self._theoretical_clusters:
            for empirical_cluster in self._empirical_clusters:
                theoretical_arids = theoretical_cluster.get_arid_list()
                theoretical_arid_set = set()
                for arid in theoretical_arids:
                    theoretical_arid_set.add(arid.get_identifier())
                empirical_arids = empirical_cluster.get_arid_list()
                empirical_arid_set = set()
                for arid in empirical_arids:
                    empirical_arid_set.add(arid.get_identifier())
                n_ij = len(theoretical_arid_set & empirical_arid_set)
                n_j = len(theoretical_arid_set)
                aap += n_ij ** 2 / n_j
        n = len(self._contained_arids)
        aap = aap / n
        return aap

    def compute_k(self) -> float:
        """
        Compute and return the K metric of this block.
        """
        acp = self.compute_average_cluster_purity()
        aap = self.compute_average_author_purity()
        k = math.sqrt(acp * aap)
        return k
