import math

from lab.function import Function


def _safety_harness(function):

    def safe_function(*args, **kwargs):
        result = 0
        try:
            result = function(*args, **kwargs)
            if isinstance(result, complex):
                result = 0
            if result > 2**16:
                result = 0
        except (ZeroDivisionError, ValueError, OverflowError, TypeError) as e:
            pass
        return result

    return safe_function


def safety_harness(function):
    return Function(_safety_harness(function.fun), function.arity)
