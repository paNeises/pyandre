import pyandre


def test_pyandre():
    arid = pyandre.Arid("1")
    cluster = pyandre.Cluster([arid])
    pyandre.BlockResult([cluster], [cluster])
