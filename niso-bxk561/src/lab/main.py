import argparse
import os
import queue
import sys

import time
from threading import Thread
from urllib.parse import quote

from evaluate_fitness import load_training_data
from genetic_algorithm import genetic_algorithm
from solution import Solution
from tree import Tree


def q1(expr, x):
    import urllib.request as r

    result = Tree(expr).evaluate(x)

    if "-test" not in sys.argv:
        # r.urlopen("http://192.168.0.69:8000/" + quote(str(expr)) + "/" + quote(str(x)))
        print(result)
    else:
        return result


def q2(expr, data):
    training_data = load_training_data(data)
    print(Solution(expr).evaluate_fitness_against(training_data))


def q3(m, data, time_budget, lambda_):
    # Load the training data specified.
    training_data = load_training_data(data)

    # Perform the genetic algorithm.
    results_queue = queue.LifoQueue()
    computation_thread = Thread(
        target=lambda: genetic_algorithm(lambda_, m, 1000, training=training_data, results_queue=results_queue),
        daemon=True  # Allow exiting when the timer runs out.
    )
    computation_thread.start()

    # Wait max. of time-budget seconds for the algorithm to finish.
    time.sleep(time_budget)
    best = results_queue.get_nowait()
    print(best.tree)


def main(args):
    expr = args.expr
    if expr and "(" not in expr:
        expr = f"({expr})"

    if args.question == 1:
        q1(expr, args.x)

    elif args.question == 2:
        q2(expr, args.data)

    elif args.question == 3:
        q3(args.m, args.data, args.time_budget, args.lambda_)


if __name__ == "__main__":

    def arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument('-n', type=int)
        parser.add_argument('-m', type=int)
        parser.add_argument('-x')
        parser.add_argument('-question', type=int)
        parser.add_argument('-expr')
        parser.add_argument('-data')
        parser.add_argument('-lambda', type=int, dest="lambda_")
        parser.add_argument('-time_budget', type=int)
        return parser.parse_args()

    if "-test" in sys.argv:
        with open("logs.txt") as f:
            for line in f:
                expr = line.strip("\n")
                inputs = next(f).strip("\n")
                print(expr, inputs, "=", q1(expr, inputs))
    else:
        main(arguments())

    # Goal: fix inequality with "diff" ✓
    # Goal: fix inequality with "avg" ✓
    # Goal: fix new inequality with "avg"


    # (avg (log -0.298627438679) (pow (ifleq 3.70220418577 4.39778904293 3.18871562135 3.00850131927) -0.567295461733))
    # -0.0601667594992 -2.33781066166 -1.85453916529 0.939992787715 0.352976104076 -0.329157709446 0.905607095496 -2.45394448168 0.347409046076 -0.388890343325
    # -0.48785240875371993

    # (avg 0 (pow 3.18871562135 -0.567295461733))

    # should be 0 apparently?
