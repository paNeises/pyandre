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
- ratio of cluster size (RCS)

# Installation

You can install the libraray via pip directly from the git repository.
We recoomend using a tagged release commit.
The package is usable starting with version tag "v0.7.0" and above.
You can install the package using Python >= 3.13 and Pip using the following command (replace `$VERSIONTAG` with the preferred version tag):

```
pip3 install git+https://github.com/paNeises/pyandre.git@$VERSIONTAG
```
