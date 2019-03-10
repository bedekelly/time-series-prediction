from collections import OrderedDict

from src.solution import Solution


def test_solution():

    training_data = OrderedDict([
        ((1, 2, 3, 4, 5), 3),
        ((2, 4, 6, 2, 11), 5)
    ])

    tests = [
        ("(avg 0 5)", 0),
        ("(add (data 0) (data 1))", 0.5),
        ("(log (data 1))", 6.5)
    ]

    for expr, expected in tests:
        solution = Solution(expr)
        returned_fitness = solution.evaluate_fitness_against(training_data)
        assert returned_fitness == expected
        assert solution.fitness == expected
