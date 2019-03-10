from src.evaluate_fitness import load_training_data
from src.generation import generate_random_solutions


def genetic_algorithm(pop_size=100, input_size=100, training=None):
    population = generate_random_solutions(pop_size, input_size)
    for solution in population:
        solution.evaluate_fitness_against(training)

    # While !terminate:
    # - stochastically sort population
    # - chop off bottom
    # - choose top n individuals to use as parents
    # - apply variation operators to get children
    # - evaluate children's fitness
    # - use crowding to replace similar individuals

    return population


def test_genetic_algorithm():
    training_data = load_training_data("data1.dat")
    solutions = genetic_algorithm(pop_size=5, input_size=5, training=training_data)

    for solution in solutions:
        print(solution)


test_genetic_algorithm()
