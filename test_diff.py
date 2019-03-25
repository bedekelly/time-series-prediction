inputs = "-0.396694184607 0.118072688623 0.728770358963 0.138306929256 -0.905062074618 1.51888833972 -1.03842261521 0.920271197065 -0.903736104757 -1.14762561029"

inputs = [float(n) for n in inputs.split()]

from itertools import permutations
for a, b in permutations(inputs, 2):
    print(a, b, a - b)


