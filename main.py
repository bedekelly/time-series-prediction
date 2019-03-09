import click
from evaluate_expression import evaluate_expression


@click.command()
@click.option('-expr', help='Expression to evaluate')
@click.option('-n', help='Dimension of the input vector')
@click.option('-x', help='The input vector')
def q1(expr, n, x):
    print(evaluate_expression(expr, x))
