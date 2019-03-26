import time

from evaluate_fitness import load_training_data
from generation import generate_random_solutions

training = load_training_data("/Users/bede/Programming/NISO/TimeSeriesPrediction/niso-bxk561/src/lab/data"
                              "/cetdl1772small.dat")

start = time.perf_counter()
population = generate_random_solutions(100, 0, max_depth=3)

for solution in population:
    solution.evaluate_fitness_against(training)
print(f"Total time: {time.perf_counter() - start}s")
