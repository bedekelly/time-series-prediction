from src.math_functions import MATH_FUNCTIONS
from src.data_functions import DATA_FUNCTIONS


def evaluate_tree(syntax_tree, input_vector=None):
    if type(syntax_tree) != list:
        return syntax_tree

    fun_key, *params = syntax_tree
    params = [evaluate_tree(param, input_vector) for param in params]

    if fun_key in MATH_FUNCTIONS:
        fun = MATH_FUNCTIONS[fun_key].fun
        return fun(*params)

    elif fun_key in DATA_FUNCTIONS:
        fun = DATA_FUNCTIONS[fun_key].fun
        return fun(*params, input_vector)

    raise ValueError("Invalid function: ", fun_key)
