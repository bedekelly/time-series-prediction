from lab.parsing import parse
from lab.math_functions import MATH_FUNCTIONS
from lab.data_functions import DATA_FUNCTIONS


class Tree:

    def __init__(self, expression):
        if type(expression) is str:
            expression = parse(expression)
        self._expression = expression

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

    def __len__(self):
        """
        Calculate the number of nodes in this tree.
        :return: The number of nodes in the tree.
        """
        if type(self._expression) is int:
            return 1
        return 1 + sum(len(param) for param in self._expression[1:])

    def __str__(self):
        """
        Display an expression like ["mul", 2, 3] as (mul 2 3).
        :return: A formatted string representation of this tree.
        """
        if type(self._expression) == int:
            return str(self._expression)
        return f"({self._expression[0]} {' '.join(map(str, self._expression[1:]))})"

    def subtree_at(self, index):
        """
        Return the subtree (and depth of that subtree) at an index.
        The index refers to a depth-first search of the subtree.
        :param index: The index of the node to find.
        :return: A tuple of (depth of node, node at index).
        """
        return 0, self._expression
