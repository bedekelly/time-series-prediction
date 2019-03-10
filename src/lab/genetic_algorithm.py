import random

from lab.evaluate_fitness import load_training_data
from lab.generation import generate_random_solutions
from lab.sorting import stochastic_sort


def mutate(child):
    return child


def crossover(parent1, parent2):
    return parent1, parent2


def breed(parents, mutation_crossover_ratio=0.3):
    """
    Apply variation operators to all parents and generate the same
    number of children.
    :param parents: The parents to be bred.
    :param mutation_crossover_ratio: The probability that we'll mutate
        the next parent instead of using crossover.
    :return: The children we've gained as a result of breeding.
    """
    children = []
    random.shuffle(parents)
    num_children = len(parents)-1

    while num_children:
        if num_children == 1 or random.random() < mutation_crossover_ratio:
            print(num_children, parents)
            parent = parents[num_children]
            child = mutate(parent)
            children.append(child)
            num_children -= 1
        else:
            parent1, parent2 = parents[num_children], parents[num_children-1]
            new_children = crossover(parent1, parent2)
            children.extend(new_children)
            num_children -= 2

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
        children = breed(parents)

        for c in children:
            c.evaluate_fitness_against(training)

        # - use crowding to replace similar individuals
        # (for now, replace lowest ranked individuals)
        population = population[:-num_children] + children

    return population


def test_genetic_algorithm():
    training_data = load_training_data("src/lab/data1.dat")
    solutions = genetic_algorithm(pop_size=100, input_size=5, number_iterations=100, training=training_data)

    for solution in solutions:
        print(solution)


test_genetic_algorithm()
