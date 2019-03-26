import math

from function import Function


def _safety_harness(function):

    def safe_function(*args, **kwargs):
        result = 0
        try:
            result = function(*args, **kwargs)
            if isinstance(result, complex):
                result = 0
            if result > 2 ** 20:
                result = 2 ** 20
        except (ZeroDivisionError, ValueError, OverflowError, TypeError):
            pass
        return result

    return safe_function


def safety_harness(function):
    return Function(_safety_harness(function.fun), function.arity)
