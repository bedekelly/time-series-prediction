import pytest

from tree import Tree


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
    assert Tree(0.0) == 0
    assert Tree(10) == 10
    assert Tree(1) == Tree(1)
    assert Tree("(mul 1 2)") == Tree("(mul 1 2)")
    assert Tree("(mul 1 2)") != Tree ("(mul (add 1 2) 2)")


def test_tree_simplify():
    assert Tree(1).simplify() == Tree(1)
    assert Tree("(mul 1 2)").simplify() == Tree(2)
    assert Tree("(mul 5 (add 2 3))").simplify() == Tree(25)
    assert Tree("(data 0)").simplify() == Tree("(data 0)")
    assert Tree("(add (data 0) 2)").simplify() == Tree("(add (data 0) 2)")
    assert Tree("(data (add 1 2))").simplify() == Tree("(data 3)")
    assert Tree("(pow 0 2)").simplify() == Tree(0)


def test_tree_lazy_simplify():
    assert Tree("(ifleq 1 2 (data 0) (data 1))").simplify() == Tree("(data 0)")
    assert Tree(
        "(add (sqrt 0) (mul (add (ifleq 2 (diff 4 0) (diff 0 2) (pow 4 0)) 4) (data (div 3 0))))"
    ).simplify() == Tree("(mul (add (ifleq 2 (diff 4 0) (diff 0 2) 1) 4) (data 0))")
    assert Tree(
        "(sub (mul (add (mul (sqrt 1) 2) 3) (avg (add 2 3) (data (max 3 2)))) (div (data (max 2 (avg 3 3))) (diff 2 ("
        "avg 0 (add 4 3))))) "
    ).simplify() == Tree("(sub (mul 5.0 (avg 5 (data 3))) (div (data (max 2 (avg 3 3))) (diff 2 (avg 0 7))))")
    assert Tree(
        "(sub (data 3) (ifleq (data (mul 0 1)) (log (data 3)) (add -8 (diff 1.0 3)) 1))"
    ).simplify() == Tree("(sub (data 3) (ifleq (data 0) (log (data 3)) (add -8 (diff 1.0 3)) 1))")
    assert Tree(
        "(add (sub 8 (diff (pow 1 (avg 4 3)) 403.4287934927351)) (data (sqrt (data 3))))"
    ).simplify() == Tree("(add (sub 8 (diff 1 403.4287934927351)) (data (sqrt (data 3))))")


if __name__ == "__main__":
    test_expression_length()
    test_subtree_at()
    test_replace_subtree_at()
    test_tree_height()
    test_tree_simplify()
    test_tree_lazy_simplify()
