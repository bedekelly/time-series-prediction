import operator
import math

from src.safety_harness import safety_harness
from src.function import Function


def ifleq(a, b, c, d):
    return c if a <= b else d


def limited_pow(a, b):
    """
    Define a "limited" version of pow, which doesn't allow powers greater
    than 1024. This seems small, but note that 2 ** (2 ** 10) is a number
    309 digits long.
    """
    if a > 2 ** 10 or b > 2 ** 10:
        return 0
    return pow(a, b)


def limited_exp(x):
    """
    Define a "limited" version of exp, which doesn't allow powers greater
    than 128. As above, this is fast.
    """
    if x > 128:
        return 0
    return math.exp(x)


MATH_FUNCTIONS = {
    "add": Function(operator.add, arity=2),
    "sub": Function(operator.sub, arity=2),
    "mul": Function(operator.mul, arity=2),
    "div": Function(operator.truediv, arity=2),
    "pow": Function(limited_pow, arity=2),
    "sqrt": Function(math.sqrt, arity=1),
    "log": Function(math.log2, arity=1),
    "exp": Function(limited_exp, arity=1),
    "max": Function(max, arity=2),
    "ifleq": Function(ifleq, arity=4)
}


for key, function in MATH_FUNCTIONS.items():
    MATH_FUNCTIONS[key] = safety_harness(function)
