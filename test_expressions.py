from main import evaluate_expression

test_cases = {
    ("(add 1 2)", ""): 3,
    ("(sub 1 2)", ""): -1,
    ("(mul 2 4)", ""): 8,
    ("(div 5 2)", ""): 2.5,
    ("(pow 10 3)", ""): 1000,
    ("(sqrt 25)", ""): 5,
    ("(log 8)", ""): 3,
    ("(exp -1)", ""): 0.36787944117144233,
    ("(max 12 14)", ""): 14,
    ("(max 18 14)", ""): 18,
    ("(ifleq 2 3 10 20)", ""): 10,
    ("(ifleq 4 3 10 20)", ""): 20,
    ("(data 2)", "10 20 30 40"): 30,
    ("(diff 1 2)", "10 20 30 40"): -10,
    ("(avg 3 7)", "1 2 3 4 5 6 7 8 9"): 5.5,

    ("(add (mul 2 3) (log 4))", ""): 8,
    ("(sqrt -1)", ""): 0,
    ("(div 1 0)", ""): 0,
    ("(avg 1 1)", "1 2 3"): 0,

    ("(avg 0 5)", "1 2 3 4 5"): 3,
    ("(avg 0 5", "2 4 6 2 11"): 5
}


def test_all_functions():
    for (expression, input_vector), result in test_cases.items():
        assert evaluate_expression(expression, input_vector) == result
