from collections import OrderedDict

from lab.solution import Solution


def test_evaluate_solution_fitness():
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


def test_mutate_solution():
    expr = "(add (mul 1 2) (sub 3 4))"
    solution = Solution(expr)
    for _ in range(10000):
        new_solution = solution.mutate()
        assert str(solution) != str(new_solution)


if __name__ == "__main__":
    test_evaluate_solution_fitness()
    test_mutate_solution()
