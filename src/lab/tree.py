from lab.parsing import parse
from lab.math_functions import MATH_FUNCTIONS
from lab.data_functions import DATA_FUNCTIONS


class Tree:

    def __init__(self, expression):
        # Parse any raw string expressions.
        if type(expression) is str:
            expression = parse(expression)

        # Use immutable data structures for speed & safety.
        if type(expression) is list:
            expression = tuple(expression)

        self._expression = expression
        self._length = None
        self._string = None
        self._length = self._calculate_length()
        self._string = self._calculate_string()

    def evaluate(self, input_vector=None):
        """
        Evaluate a tree's value given a vector of input data.
        :param input_vector: The given input data.
        :return: The tree's final evaluated value.
        """
        # If we're just an int wrapper, return the int.
        if type(self._expression) is int:
            return self._expression

        if type(self._expression) is type(self):
            return self._expression.evaluate(input_vector)

        if type(input_vector) is str:
            input_vector = tuple(float(x) for x in input_vector.strip().split())

        fun_key, *params = self._expression
        params = [param.evaluate(input_vector) for param in params]

        if fun_key in MATH_FUNCTIONS:
            fun = MATH_FUNCTIONS[fun_key].fun
            return fun(*params)

        elif fun_key in DATA_FUNCTIONS:
            fun = DATA_FUNCTIONS[fun_key].fun
            return fun(*params, input_vector)

        raise ValueError("Invalid function: ", fun_key)

    def _calculate_length(self):
        """
        Calculate the number of nodes in this tree.
        :return: The number of nodes in the tree.
        """
        if type(self._expression) is int:
            return 1
        return 1 + sum(len(param) for param in self._expression[1:])

    def _calculate_string(self):
        """
        Display an expression like ["mul", 2, 3] as (mul 2 3).
        :return: A formatted string representation of this tree.
        """
        if type(self._expression) == int:
            return str(self._expression)
        return f"({self._expression[0]} {' '.join(map(str, self._expression[1:]))})"

    def __len__(self):
        return self._length

    def __str__(self):
        return self._string

    def replace_subtree_at(self, index, new_subtree):
        """
        Replace a node with a new subtree.
        :param index: The index of the node to replace.
        :param new_subtree: The new node to replace it with.
        :return: A tree with the solution replaced.
        """

        # Check the index is actually in this tree.
        if index >= self._length:
            raise IndexError(f"Index out of bounds: {index} (max {self._length - 1})")

        # If we're replacing the whole tree, do it here.
        if index == 0:
            return new_subtree

        # Count the current node.
        index -= 1

        # Build a new expression list, recursively replacing the subtree once.
        new_expression_list = [self._expression[0]]
        found = False
        for subtree in self._expression[1:]:
            if not found and index < len(subtree):
                found = True
                subtree = subtree.replace_subtree_at(index, new_subtree)
            else:
                index -= len(subtree)
            new_expression_list.append(subtree)

        return Tree(new_expression_list)

    def subtree_at(self, index, _depth=0):
        """
        Return the subtree (and depth of that subtree) at an index.
        The index refers to a depth-first search of the subtree.
        :param index: The index of the node to find.
        :param _depth: The depth of the current node.
        :return: A tuple of (depth of node, node at index).
        """

        # Check the index is actually in this tree.
        if index >= self._length:
            raise IndexError(f"Index out of bounds: {index} (max {self._length - 1})")

        # An index of 0 means the root node.
        if index == 0:
            return _depth, self

        # Count the current node.
        index -= 1

        # Look for the tree that the index will be in.
        for tree in self._expression[1:]:
            if index < len(tree):
                depth, subtree = tree.subtree_at(index, _depth + 1)
                break
            else:
                index -= len(tree)
        else:
            raise IndexError("Got to the end without finding it!")

        return depth, subtree