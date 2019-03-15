import queue
import time
from threading import Thread

import click

from lab.evaluate_fitness import load_training_data
from lab.genetic_algorithm import genetic_algorithm
from lab.solution import Solution
from lab.tree import Tree


@click.group()
def main():
    pass


@main.command()
@click.option('-expr', help='Expression to evaluate')
@click.option('-n', help='Dimension of the input vector')
@click.option('-x', help='The input vector')
def q1(expr, _, x):
    print(Tree(expr).evaluate(x))


@main.command()
@click.option('-expr', help='Expression to evaluate')
@click.option('-n', help='Dimension of the input vector')
@click.option('-m', help="Size of the training data")
@click.option('-data', help="Filename of the training data")
def q2(expr, _, _, data):
    training_data = load_training_data(data)
    print(Solution(expr).evaluate_fitness_against(training_data))


@main.command()
@click.option('-lambda', help="Population size")
@click.option('-n', help="Dimension of the input vector")
@click.option('-m', help="Size of the training data")
@click.option('-data', help="Filename of the training data")
@click.option('-time_budget', help="Time budget for the algorithm")
def q3(_, m, data, time_budget, **kwargs):

    # Normalise our cli-arguments.
    m = int(m)
    lambda_ = int(kwargs["lambda"])

    # Load the training data specified.
    training_data = load_training_data(data)

    # Perform the genetic algorithm.
    results_queue = queue.LifoQueue()
    computation_thread = Thread(
        target=lambda: genetic_algorithm(lambda_, m, 1000, training=training_data, results_queue=results_queue),
        daemon=True  # Allow exiting when the timer runs out.
    )
    computation_thread.start()

    # Wait max. of time-budget seconds for the algorithm to finish.
    time.sleep(int(time_budget))
    best = results_queue.get_nowait()
    print(best.tree)


if __name__ == "__main__":
    main()
