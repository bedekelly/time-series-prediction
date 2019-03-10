from collections import OrderedDict

from src.evaluate_fitness import evaluate_fitness_against_data


def test_simple_fitness_evaluation():
    training_data = OrderedDict([
        ((), 5),
        ((1.0, 3.0), 5)
    ])
    assert evaluate_fitness_against_data("(add 2 3)", training_data) == 0
    assert evaluate_fitness_against_data("(add 4 4)", training_data) == 9


def test_data_fitness_evaluation():
    training_data = OrderedDict([
        ((1, 2, 3, 4, 5), 3),
        ((2, 4, 6, 2, 11), 5)
    ])

    tests = [
        ("(avg 0 5)", 0),
        ("(add (data 0) (data 1))", 0.5),
        ("(log (data 1))", 6.5)
    ]

    for expression, result in tests:
        assert evaluate_fitness_against_data(expression, training_data) == result
