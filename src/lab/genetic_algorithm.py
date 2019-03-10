import random

from lab.evaluate_fitness import load_training_data
from lab.generation import generate_random_solutions
from lab.sorting import stochastic_sort


def breed(parents, mutation_crossover_ratio=1):
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
    num_children = len(parents)

    while num_children:
        if num_children == 1 or random.random() < mutation_crossover_ratio:
            parent = parents[num_children-1]
            child = parent.mutate()
            children.append(child)
            num_children -= 1
        else:
            parent1, parent2 = parents[num_children-1], parents[num_children-2]
            new_children = parent1.crossover(parent2)
            children.extend(new_children)
            num_children -= 2

    return children


def genetic_algorithm(pop_size=100, input_size=100, number_iterations=100, num_parents=0.3, training=None):
    """
    Run an independent instance of the genetic algorithm.
    :param pop_size: The size of the population to evolve.
    :param input_size: The size of the input vectors in the training data.
    :param number_iterations: The number of generations of evolution.
    :param num_parents: Number of parents chosen from the population each generation,
        as a fraction of the population size.
    :param training: The training data.
    :return: The population of the final generation.
    """
    population = generate_random_solutions(pop_size, input_size)
    num_children = num_parents = int(pop_size * num_parents)

    for solution in population:
        solution.evaluate_fitness_against(training)

    for i in range(number_iterations):
        # - Check termination condition
        assert len(population) == pop_size
        population = stochastic_sort(population)
        assert len(population) == pop_size

        parents = population[:num_parents]
        assert parents

        children = breed(parents)
        assert len(children) == len(parents)

        for c in children:
            c.evaluate_fitness_against(training)

        # - use crowding to replace similar individuals
        # (for now, replace lowest ranked individuals)
        population = population[:-num_children] + children

    return population


def test_genetic_algorithm(tests=1):
    training_data = load_training_data("src/lab/average.dat")

    solutions = []

    print("[", end='')
    for _ in range(tests):
        solutions = genetic_algorithm(pop_size=100, input_size=5, number_iterations=1000, training=training_data)
        print(".", end='')
    print("]")

    for s in solutions:
        print(s)


if __name__ == "__main__":
    test_genetic_algorithm(1)
