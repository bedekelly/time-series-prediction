import pytest

from lab.tree import Tree


def test_expression_length():
    assert len(Tree(1)) == 1
    assert len(Tree("(mul 1 2)")) == 3
    assert len(Tree("(add (mul 1 2) (sub 3 4))")) == 7


def test_subtree_at():
    t = Tree("(mul (add 1 2) (sub (div 8 2) 4))")
    assert len(t) == 9
    with pytest.raises(IndexError):
        t.subtree_at(9)

    depth, tree = t.subtree_at(4)
    assert depth == 1
    assert str(tree) == "(sub (div 8 2) 4)"

    depth, tree = t.subtree_at(0)
    assert depth == 0
    assert str(tree) == str(t)

    depth, tree = t.subtree_at(5)
    assert depth == 2
    assert str(tree) == "(div 8 2)"

    depth, tree = t.subtree_at(7)
    assert depth == 3
    assert str(tree) == "2"


def test_replace_subtree_at():
    t = Tree("(mul (add 1 2) (sub (div 8 2) 4))")
    new_tree = t.replace_subtree_at(0, Tree(1))
    assert str(new_tree) == "1"
    assert len(new_tree) == 1

    new_tree = t.replace_subtree_at(4, Tree("(add 3 4)"))
    assert str(new_tree) == "(mul (add 1 2) (add 3 4))"
    assert len(new_tree) == 7

    new_tree = t.replace_subtree_at(7, Tree("(add 1 2)"))
    assert str(new_tree) == "(mul (add 1 2) (sub (div 8 (add 1 2)) 4))"
    assert len(new_tree) == 11

    new_tree = t.replace_subtree_at(3, Tree(5))
    assert str(new_tree) == "(mul (add 1 5) (sub (div 8 2) 4))"
    assert len(new_tree) == 9


def test_tree_height():
    assert Tree("(mul (add 1 2) (sub (div 8 2) 4))").height == 3
    assert Tree(1).height == 0


def test_tree_equality():
    assert Tree(1) == Tree(1)
    assert Tree("(mul 1 2)") == Tree("(mul 1 2)")
    assert Tree("(mul 1 2)") != Tree ("(mul (add 1 2) 2)")


if __name__ == "__main__":
    test_expression_length()
    test_subtree_at()
    test_replace_subtree_at()
    test_tree_height()
