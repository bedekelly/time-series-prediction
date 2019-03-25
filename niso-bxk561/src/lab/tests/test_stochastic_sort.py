from sorting import stochastic_sort


class DummySolution:
    def __init__(self, value):
        self.fitness = value

    def __str__(self):
        return str(self.fitness)

    __repr__ = __str__


solutions = [DummySolution(i) for i in range(100)]
sorted_solutions = stochastic_sort(solutions)
print(sorted_solutions)
