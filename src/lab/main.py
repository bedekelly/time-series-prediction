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
def q2(expr, n, m, data):
    training_data = load_training_data(data)
    print(Solution(expr).evaluate_fitness_against(training_data))


@main.command()
@click.option('-lambda', help="Population size")
@click.option('-n', help="Dimension of the input vector")
@click.option('-m', help="Size of the training data")
@click.option('-data', help="Filename of the training data")
@click.option('-time_budget', help="Time budget for the algorithm")
def q3(n, m, data, time_budget, **kwargs):

    global best
    global training_data
    global fitness_separately

    # Normalise our cli-arguments.
    n = int(n)
    m = int(m)
    lambda_ = int(kwargs["lambda"])

    # Load the training data specified.
    training_data = load_training_data(data)

    # Perform the genetic algorithm.
    best = genetic_algorithm(lambda_, m, 1000, training=training_data)
    print(best)

    # Check that we evaluated the fitness correctly.
    fitness_separately = Solution(str(best.expression_tree)).evaluate_fitness_against(training_data)
    if best.fitness != fitness_separately:
        print("Different")
        print(best)
        print(fitness_separately)
        import pdb; pdb.set_trace()


if __name__ == "__main__":
    main()
