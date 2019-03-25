import csv
from statistics import mean
from collections import OrderedDict


def mean_square_error(seq1, seq2):
    try:
        return mean((a - b) ** 2 for a, b in zip(seq1, seq2))
    except OverflowError:
        return 2 ** 100


def evaluate_fitness_against_data(expression, training_data):
    calculated_results = [expression.evaluate(input_vector) for input_vector in training_data]
    target_results = training_data.values()
    return mean_square_error(calculated_results, target_results)


def load_training_data(filename):
    training_data = OrderedDict()
    with open(filename) as f:
        for line in csv.reader(f, delimiter='\t'):
            *input_vector, output = line
            key = tuple(map(float, input_vector))
            training_data[key] = float(output)
    return training_data


def evaluate_fitness_against_file(expression, training_data_file):
    training_data = load_training_data(training_data_file)
    return evaluate_fitness_against_data(expression, training_data)
