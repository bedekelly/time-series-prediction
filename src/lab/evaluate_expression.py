import sexpdata

from lab.evaluate_tree import evaluate_tree


def normalise_tree(tree):
    if type(tree) is int:
        return tree
    fun, *params = tree
    return [fun.value(), *(map(normalise_tree, params))]


def parse(expression):
    return normalise_tree(sexpdata.loads(expression))


def evaluate_expression(expression, input_vector):
    if type(input_vector) is str:
        input_vector = tuple(float(x) for x in input_vector.strip().split())
    syntax_tree = parse(expression)
    result = evaluate_tree(syntax_tree, input_vector)
    return result


