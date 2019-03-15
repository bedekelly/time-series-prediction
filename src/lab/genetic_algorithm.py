import random
from math import floor

from lab.generation import generate_random_solutions
from lab.sorting import stochastic_sort


def breed(parents, mutation_crossover_ratio=0.5):
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
            child1, child2 = parent1.crossover(parent2)
            children.extend([child1, child2])
            num_children -= 2

    return children


def genetic_algorithm(pop_size=100, input_size=100, number_iterations=100, fraction_parents=0.1, p_simplify=0.01,
                      training=None, results_queue=None):
    """
    Run an independent instance of the genetic algorithm.
    :param pop_size: The size of the population to evolve.
    :param input_size: The size of the input vectors in the training data.
    :param number_iterations: The number of generations of evolution.
    :param fraction_parents: Fraction of parents chosen from the population each generation
    :param training: The training data.
    :param p_simplify: The likelihood of simplifying a solution each generation.
    :param results_queue: A results queue to populate with the current best solution.
    :return: The population of the final generation.
    """

    population = generate_random_solutions(pop_size, input_size)
    num_children = num_parents = floor(pop_size * fraction_parents)

    for solution in population:
        solution.evaluate_fitness_against(training)
    best_so_far = population[0].simplify()

    for i in range(number_iterations):
        population = stochastic_sort(population)

        # Simplify each expression with some probability each generation.
        population = [p.simplify() if random.random() < p_simplify else p for p in population]

        # Check for a new best-ever solution.
        for solution in population:
            better_fitness = solution.fitness < best_so_far.fitness
            same_fitness_simpler = solution.fitness == best_so_far.fitness and solution.length < best_so_far.length
            if better_fitness or same_fitness_simpler:
                best_so_far = solution

        if results_queue is not None:
            results_queue.put(best_so_far)

        # Pick parents and breed to get children.
        parents = population[:num_parents]
        children = breed(parents)
        for c in children:
            c.evaluate_fitness_against(training)

        # - use crowding to replace similar individuals
        # (for now, replace lowest ranked individuals)
        population = population[:-num_children] + children

    return best_so_far
