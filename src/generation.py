import random

from src.solution import Solution
from src.math_functions import MATH_FUNCTIONS
from src.data_functions import DATA_FUNCTIONS


def generate_random_solutions(n, input_size, max_depth=10):
    """
    Generate random functions of input data.
    :param n: The number of random solutions to generate.
    :param input_size: The size of each input vector.
    :param max_depth: The maximum depth of any expression tree.
    :return: A sequence of random, *valid* expressions.
    """

    def random_number():
        return random.randrange(0, input_size)

    def random_function():
        return random.choice([*MATH_FUNCTIONS.items(), *DATA_FUNCTIONS.items()])

    def create_random_node(depth):
        if random.random() < depth / max_depth:
            return random_number()
        name, (_, arity) = random_function()
        return [name, *create_random_nodes(arity, depth + 1)]

    def create_random_nodes(num_nodes, depth=0):
        return [create_random_node(depth) for i in range(num_nodes)]

    return [Solution(node) for node in create_random_nodes(n)]
