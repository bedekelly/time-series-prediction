from lab.tree import Tree


def test_expression_length():
    assert len(Tree(1)) == 1
    assert len(Tree("(mul 1 2)")) == 3
    assert len(Tree("(add (mul 1 2) (sub 3 4))")) == 7
