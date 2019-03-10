import math

from function import Function


def _safety_harness(function):

    def safe_function(*args, **kwargs):
        result = 0
        try:
            result = function(*args, **kwargs)
            if math.isnan(result):
                result = 0
        except (ZeroDivisionError, ValueError, OverflowError, TypeError) as e:
            # print("Caught error:", e)
            pass
        return result

    return safe_function


def safety_harness(function):
    return Function(_safety_harness(function.fun), function.arity)
