import random

from lab.evaluate_fitness import load_training_data
from lab.generation import generate_random_solutions
from lab.sorting import stochastic_sort


def breed(parents, num_children):
    # Apply variation operators to parents to get children.
    return [p for p in parents]


def genetic_algorithm(pop_size=100, input_size=100, number_iterations=100, num_parents=0.3, training=None):
    population = generate_random_solutions(pop_size, input_size)
    num_children = num_parents = int(input_size * num_parents)

    for solution in population:
        solution.evaluate_fitness_against(training)

    for i in range(number_iterations):
        # - Check termination condition
        population = stochastic_sort(population)

        parents = population[:num_parents]
        children = breed(parents, num_children)

        for c in children:
            c.evaluate_fitness_against(training)

        # - use crowding to replace similar individuals

    return population


def test_genetic_algorithm():
    training_data = load_training_data("src/lab/data1.dat")
    solutions = genetic_algorithm(pop_size=100, input_size=5, number_iterations=1, training=training_data)

    for solution in solutions:
        print(solution)


test_genetic_algorithm()
