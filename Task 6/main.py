import math


def main(y):
    n = len(y) - 1
    return 22 * sum(44 * math.atan(46 * y[int(n + 1 - i)]) ** 4 for i in range(1, len(y) - 1))


print(main([0.64, -0.74, -0.72, -0.2, -0.77, 0.98, -0.18, 0.48]))
print(2.92e+04)