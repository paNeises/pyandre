# About

This repository contains a PYthon library for Author Name Disambiguation Result Evaluation (pyandre).
It implements the evaluation metrics as described in chapter 2.3 of the book "Automatic Disambiguation of Author Names in Bibliographic Repositories" by Ferreira et al. ([available here](https://doi.org/10.2200/S01011ED1V01Y202005ICR070))

## Currently implemented metrics

- average cluster purity (ACP)
- average author purity (AAP)
- K
- pairwise precision (pP)
- pairwise recall (pR)
- pairwise F1 (pF1)
- cluster precision (cP)
- cluster recall (cR)
- cluster F1 (cF1)
- ratio of cluster size (RCS)
- B-Cubed precision (bP)
- B-Cubed recall (bR)
- B-Cubed F (bFa)

# Installation

You can install the libraray via pip directly from the git repository.
We recommend using a tagged release commit.
The package is usable starting with version tag "v0.7.0" and above.
You can install the package using Python >= 3.13 and Pip using the following command (replace `$VERSIONTAG` with the preferred version tag):

```
pip3 install git+https://github.com/paNeises/pyandre.git@$VERSIONTAG
```

# Usage

The class responsible for the evaluation is the Result class.
It gets provided with a list of theoretical clusters representing the correct authors, and a list of empirical clusters representing the authors obtained by the author name disambiguation algorithm that should be evaluated.
These two lists are lists of objects of the Cluster class.
Each cluster class is initialized with a list of authorship record ID's, represented by the Arid class.
The Arid objects are initialized with a string identifier.
Two Arid objects are assumed to be the same, when their string identifier matches.
Below you can find a minimal code example on how to use the library:

```
import pyandre


# Create theoretical Arid's
t_arid_1 = pyandre.Arid("1")
t_arid_2 = pyandre.Arid("2")
t_arid_3 = pyandre.Arid("3")
t_arid_4 = pyandre.Arid("4")
t_arid_5 = pyandre.Arid("5")
t_arid_6 = pyandre.Arid("6")
t_arid_7 = pyandre.Arid("7")
t_arid_8 = pyandre.Arid("8")
t_arid_9 = pyandre.Arid("9")

# Create theoretical clusters
t_cluster_1 = pyandre.Cluster([t_arid_1, t_arid_2, t_arid_3, t_arid_4])
t_cluster_2 = pyandre.Cluster([t_arid_5, t_arid_6, t_arid_7])
t_cluster_3 = pyandre.Cluster([t_arid_8, t_arid_9])

# Create empirical Arid's
e_arid_1 = pyandre.Arid("1")
e_arid_2 = pyandre.Arid("2")
e_arid_3 = pyandre.Arid("3")
e_arid_4 = pyandre.Arid("4")
e_arid_5 = pyandre.Arid("5")
e_arid_6 = pyandre.Arid("6")
e_arid_7 = pyandre.Arid("7")
e_arid_8 = pyandre.Arid("8")
e_arid_9 = pyandre.Arid("9")

# Create empirical clusters
e_cluster_1 = pyandre.Cluster([t_arid_1, t_arid_2, t_arid_3])
e_cluster_2 = pyandre.Cluster([t_arid_5, t_arid_6, t_arid_7])
e_cluster_3 = pyandre.Cluster([t_arid_4, t_arid_8])
e_cluster_4 = pyandre.Cluster([t_arid_9])

# Create result
result = pyandre.Result([t_cluster_1, t_cluster_2, t_cluster_3], [e_cluster_1, e_cluster_2, e_cluster_3, e_cluster_4])

# Print metrics
print(result.compute_average_cluster_purity())
print(result.compute_average_author_purity())
print(result.compute_k())
print(result.compute_pairwise_precision())
print(result.compute_pairwise_recall())
print(result.compute_pairwise_f1())
print(result.compute_cluster_precision())
print(result.compute_cluster_recall())
print(result.compute_cluster_f1())
print(result.compute_ratio_of_cluster_size())
print(result.compute_bp())
print(result.compute_br())
print(result.compute_bfa())
```
