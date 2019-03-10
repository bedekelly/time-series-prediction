from lab.evaluate_tree import evaluate_tree
from lab.evaluate_fitness import evaluate_fitness_against_data

from lab.evaluate_expression import parse


class Solution:
    def __init__(self, expression_tree):
        if type(expression_tree) is str:
            expression_tree = parse(expression_tree)
        self.expression_tree = expression_tree
        self.fitness = None

    def __str__(self):
        expression = self.show(self.expression_tree)
        return f"Solution(fitness={self.fitness}, expression={expression})"

    @staticmethod
    def show(expression):
        if type(expression) == int:
            return str(expression)
        return f"({expression[0]} {' '.join(map(Solution.show, expression[1:]))})"

    def evaluate(self, input_vector):
        return evaluate_tree(self.expression_tree, input_vector)

    def evaluate_fitness_against(self, training_data):
        self.fitness = evaluate_fitness_against_data(self.expression_tree, training_data)
        return self.fitness
