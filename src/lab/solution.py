from random import randrange

from lab.evaluate_fitness import evaluate_fitness_against_data
from lab.parsing import parse
from lab.tree import Tree


class Solution:
    def __init__(self, expression_tree):
        if type(expression_tree) is str:
            expression_tree = Tree(expression_tree)
        self.expression_tree = expression_tree
        self.fitness = None

    def __str__(self):
        return f"Solution(fitness={self.fitness}, tree={self.expression_tree})"

    def evaluate(self, input_vector):
        return self.expression_tree.evaluate(input_vector)

    def evaluate_fitness_against(self, training_data):
        self.fitness = evaluate_fitness_against_data(self.expression_tree, training_data)
        return self.fitness

    # def subtree_at(self, index):
    #     return subtree_at(self.expression_tree, index)

    def mutate(self):
        """
        Return a mutated version of this solution.
        :return: A mutated solution.
        """
        random_index = randrange(len(self.expression_tree))
        node, height = self.expression_tree.subtree_at(random_index)

        # Create a random node with max_depth=(max_depth-height)
        # Replace initial node with the one we've created in a new tree
        # Create & return a Solution with that tree
        return 1
