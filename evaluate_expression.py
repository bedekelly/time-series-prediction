import sexpdata

from evaluate_tree import evaluate_tree


def normalise_tree(tree):
    if type(tree) is int:
        return tree
    fun, *params = tree
    return [fun.value(), *(map(normalise_tree, params))]


def evaluate_expression(expression, input_vector):
    if type(input_vector) is str:
        input_vector = tuple(float(x) for x in input_vector.strip().split())
    syntax_tree = normalise_tree(sexpdata.loads(expression))
    result = evaluate_tree(syntax_tree, input_vector)
    return result


