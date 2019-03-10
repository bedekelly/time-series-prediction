from random import randrange

from lab.evaluate_fitness import evaluate_fitness_against_data

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

    def mutate(self):
        """
        Return a mutated version of this solution.
        :return: A mutated solution.
        """

        # Prevent circular imports.
        from lab.generation import create_random_node, MAX_DEPTH

        # Pick a random node and get its depth.
        random_index = randrange(len(self.expression_tree))
        node_depth, subtree = self.expression_tree.subtree_at(random_index)

        # Create a random node with an appropriate max-depth.
        max_possible_depth = MAX_DEPTH - node_depth
        max_depth = max(subtree.height * 2, MAX_DEPTH - node_depth)
        random_tree = create_random_node(max_depth=max_depth)

        # Replace initial node with the one we've created in a new tree
        new_tree = self.expression_tree.replace_subtree_at(random_index, random_tree)

        # Create & return a Solution with that tree
        return Solution(new_tree)

    def crossover(self, other):
        raise NotImplemented("Crossover doesn't work yet!")
