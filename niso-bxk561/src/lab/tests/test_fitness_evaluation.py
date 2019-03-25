from collections import OrderedDict

from evaluate_fitness import evaluate_fitness_against_data, load_training_data
from generation import create_random_nodes
from solution import Solution
from tree import Tree


def test_simple_fitness_evaluation():
    training_data = OrderedDict([
        ((), 5),
        ((1.0, 3.0), 5)
    ])
    assert evaluate_fitness_against_data(Tree("(add 2 3)"), training_data) == 0
    assert evaluate_fitness_against_data(Tree("(add 4 4)"), training_data) == 9


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
        assert evaluate_fitness_against_data(Tree(expression), training_data) == result


def test_simplifying_fitness():
    nodes = create_random_nodes(1000)
    training_data = load_training_data("src/lab/data/linear_extrapolation.dat")
    for n in nodes:
        solution = Solution(n)
        solution.evaluate_fitness_against(training_data)
        simple = solution.simplify().simplify().simplify().simplify()
        if solution.fitness != simple.fitness:
            print()
            print(solution, str(solution))
            print(simple, str(simple))
        assert solution.fitness == simple.fitness


def test_weird_mutation_bug():
    training_data = OrderedDict(
        [((0.0, 1.0, 4.0, 9.0, 16.0), 25.0), ((100.0, 121.0, 144.0, 169.0, 196.0), 225.0),
         ((1000.0, 10201.0, 10404.0, 10609.0), 11025.0)])
    solution = Solution("(pow 1 (avg 4 3))")
    first = solution
    solution.evaluate_fitness_against(training_data)
    solution.simplify()
    second = solution
    assert str(first) == str(second)


def test_weird_fitness_bug():
    training_data = OrderedDict(
        [((0.0, 1.0, 4.0, 9.0, 16.0), 25.0), ((100.0, 121.0, 144.0, 169.0, 196.0), 225.0),
         ((1000.0, 10201.0, 10404.0, 10609.0), 11025.0)])

    solution = Solution("(pow 1 (avg 4 3))")
    simplified = Solution("1")
    assert solution.evaluate((1000.0, 10201.0, 10404.0, 10609.0)) == simplified.evaluate((1000.0, 10201.0, 10404.0, 10609.0))
    solution.evaluate_fitness_against(training_data)
    simplified.evaluate_fitness_against(training_data)
    auto_simplified = solution.simplify()
    assert solution.fitness == simplified.fitness == auto_simplified.fitness


def test_complex_fitness_bug():
    training_data = OrderedDict(
        [((0.0, 1.0, 4.0, 9.0, 16.0), 25.0), ((100.0, 121.0, 144.0, 169.0, 196.0), 225.0),
         ((1000.0, 10201.0, 10404.0, 10609.0), 11025.0)])
    solution = Solution("(add (sub 8 (diff (pow 1 (avg 4 3)) 403.4287934927351)) (data (sqrt (data 3))))")
    simplified = Solution("(add (sub 8 (diff 1 403.4287934927351)) (data (sqrt (data 3))))")
    solution.evaluate_fitness_against(training_data)
    simplified.evaluate_fitness_against(training_data)
    assert solution.fitness == simplified.fitness


def test_another_weird_fitness_bug():
    training_data = OrderedDict(
        [((0.0, 1.0, 4.0, 9.0, 16.0), 25.0), ((100.0, 121.0, 144.0, 169.0, 196.0), 225.0),
         ((1000.0, 10201.0, 10404.0, 10609.0), 11025.0)])
    solution = Solution("(mul (pow (sqrt (mul (log 1) 4)) (avg (sub 3 (diff 0 4)) 2)) (log 3))")
    solution.evaluate_fitness_against(training_data)
    simplified = solution.simplify()
    assert solution.fitness == simplified.fitness


def test_different_fitness_bug():
    """
    Bug fixed by altering the pow() function's behaviour to
    """
    training_data = OrderedDict([((1.0, 0.0, -1.0, -2.0, -3.0), -4.0)])
    solution = Solution("(pow 0 (pow (data 1) 2))")
    simplified = Solution("0.0")
    print(solution, simplified)
    assert solution.evaluate_fitness_against(training_data) == simplified.evaluate_fitness_against(training_data)


def test_other_fitness_bug():
    """
    Solution(fitness=45321.5, tree=(pow (diff (ifleq 2 4 4 (add 1 4)) (log (data 1))) 0))
    Solution(fitness=45306.125, tree=1)
    """
    original = Solution("(pow (diff (ifleq 2 4 4 (add 1 4)) (log (data 1))) 0)")
    training_data = OrderedDict([
        ((10.0, 20.0, 30.0, 40.0, 50.0), 60.0)
    ])
    original_fitness = original.evaluate_fitness_against(training_data)
    simplified = original.simplify()

    for key in training_data:
        o = original.evaluate(key)
        s = simplified.evaluate(key)
        assert o == s
    simplified_fitness = simplified.evaluate_fitness_against(training_data)
    assert original_fitness == simplified_fitness
