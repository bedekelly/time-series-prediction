from tree import Tree

test_cases = {

    ("(data 2)", "10 20 30 40"): 30,
    ("1.5", ""): 1.5,
    ("1.26199125402", ""): 1.26199125402,
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

    ("(diff 1 2)", "10 20 30 40"): -10,
    ("(avg 3 7)", "1 2 3 4 5 6 7 8 9"): 5.5,

    ("(add (mul 2 3) (log 4))", ""): 8,
    ("(sqrt -1)", ""): 0,
    ("(div 1 0)", ""): 0,
    ("(avg 1 1)", "1 2 3"): 0,

    ("(avg 0 5)", "1 2 3 4 5"): 0,  # Sad but this is how the reference implementation works.

    # The following tests were found by random generation of solutions.

    # Check this doesn't cause an OverflowError.
    ("(max (sqrt (exp (ifleq 7 3 (data 1) (mul 0 1)))) (sub (sub (sqrt (sub (div 9 3) (div 0 8))) (add (sqrt (ifleq 2 "
     "1 (pow 3 (ifleq 6 (div 2 1) (exp 8) 4)) 3)) (pow (max (sqrt 7) (exp 4)) 4))) (log (div (sub (div 3 (max 0 (data "
     "8))) 9) (ifleq (sub 7 (log (data 2))) 0 6 (mul 6 (pow 6 (pow 9 4))))))))", "0 1 2 3 4 5 6 7 8 9"): 1,

    # Check this doesn't cause an IndexError.
    ("(add (ifleq 9 (max 2 3) (max (exp (ifleq 7 9 4 7)) (max (ifleq (mul (div 8 6) (max (log (div 6 7)) 1)) (exp ("
     "add (avg 5 7) 3)) (diff 3 6) 2) (ifleq 7 (add (max 6 6) 4) 4 8))) (log (pow (add 0 (exp 0)) 8))) (diff (exp ("
     "add 5 (sub 2 (max (max 4 5) 6)))) (add (max 5 (ifleq (log (exp 0)) (max 7 (sqrt 3)) 1 4)) 5)))",
     "0 1 2 3 4 5 6 7 8 9"): 2,

    # Check this doesn't cause a TypeError (pow() can create complex numbers).
    ("(data (add (div (data 6) (diff (max (sqrt 5) (avg (avg 8 3) 2)) 4)) (pow (diff (avg (avg (mul (data 3) 6) 0) ("
     "sqrt 1)) (diff 8 (exp 3))) (add (avg 2 (data 6)) (avg (pow (mul (ifleq 5 2 (data 8) 3) (ifleq 2 3 5 7)) (log "
     "0)) (div (data (log 7)) (pow 3 6)))))))", "0 1 2 3 4 5 6 7 8 9"): 6,

    # Check this actually completes.
    ("(add (ifleq (add 8 32) (ifleq 82 (pow (data (exp (div 73 56))) (max (ifleq 13 12 12 (add 32 12)) 97)) (sqrt ("
     "log 82)) 91) (max 51 (diff (ifleq 64 (mul 36 20) (pow (ifleq 78 7 (add (data (data 95)) 29) 95) (sqrt (data "
     "2))) (data 50)) (diff (div 98 (sub 57 15)) (pow (exp 92) 21)))) (diff (div (div 42 (max (sqrt 17) (diff 79 "
     "32))) (pow (max 74 86) (ifleq 75 65 (max 42 (diff 25 4)) 77))) (exp (sqrt 89)))) (sqrt (sub (max (pow 7 (sub ("
     "pow 63 46) 71)) 27) (exp 98))))", ' '.join(map(str, range(100)))): -6.0,

    # Check this isn't complex.
    ("(pow (ifleq (mul (exp (mul (log (diff 4 2)) (data 1))) 3) (pow (sub (diff (pow 1 2) (exp 0)) 0) 2) (sub (sub ("
     "sub 0 3) (exp (pow (max 4 2) (exp 3)))) (add 4 (div (diff 0 0) (log 3)))) (sub 3 (exp 2))) (div (add (add (exp "
     "(sqrt 0)) (add 0 1)) (diff (avg (sqrt 4) 2) (mul (pow (exp (ifleq 4 4 3 0)) 0) 4))) 3))", "2 2 2 2 2"): 0,

    # Test cases found with docker container test script:
    ("(diff -4.02427530278 (add -4.60886792755 -2.89857290793))",
     "-1.62970614417 0.430159562734 0.651938201758 -1.15313034194 0.501951873497 -0.317562397208 1.01300412099 "
     "-0.716810712548 -0.855601205183 -0.466478879695"): 0.538038807975,

    ("(div (diff (avg 2.11255941387 -1.57291848512) -1.4134949161) (exp (sub (ifleq 2.38392075486 2.38392075486 "
     "3.41923598551 2.22079668592) (ifleq 0.222228408355 -1.55628589857 -1.56325982153 -2.05309802918))))",
     "0.352135393781 0.796653027098 0.571455271483 -0.756355218474 -1.60877877018 -0.46803749938 0.994100517348 "
     "-1.82975200209 -0.285483809168 -1.312477298"): -0.0009214537235189878,

    ("(pow 0 0)", "0"): 1,
    ("(pow 8 7)", "0"): 2097152,

    ("(diff (div (max -2.01269424741 1.37021004862) (ifleq (avg -0.27678989738 -0.757900550221) -0.911054386276 "
     "-0.281161796367 -0.757900550221)) (log 1.10792897791))", "-0.805079088563 -0.181039810198 -0.0840191620354 "
                                                               "1.58204059287 -0.424215793034 0.0902021243537 "
                                                               "0.500835874599 -0.889514499333 -2.49662351325 "
                                                               "-1.23262241715"): 0.7210599265276001
}


def test_all_functions():
    for (expression, input_vector), result in test_cases.items():
        assert Tree(expression).evaluate(input_vector) == result


if __name__ == "__main__":
    test_all_functions()
