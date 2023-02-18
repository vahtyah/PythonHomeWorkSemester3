import math


def main(y, z):
    return sum(((z[len(y) - math.ceil(i / 2)])
                ** 2 + y[math.ceil(i / 3) - 1] + 58 *
                (y[math.ceil(i / 2) - 1]) ** 3) ** 4
               for i in range(1, len(y) + 1))

print(main([-0.71, 0.8, 0.72, 0.46, -0.51, -0.57, -0.9], [-0.32, -0.34, 0.31, -0.06, -0.51, -0.9, 0.13]))
print(2.71e+06)

import math


def main(y, z, i=1):
    if i > len(y):
        return 0
    return ((z[len(y) - math.ceil(i / 2)]) ** 2 + y[math.ceil(i / 3) - 1] + 58 * (y[math.ceil(i / 2) - 1]) ** 3) ** 4\
        + main(y, z, i + 1)


print(main([-0.71, 0.8, 0.72, 0.46, -0.51, -0.57, -0.9], [-0.32, -0.34, 0.31, -0.06, -0.51, -0.9, 0.13]))
print(2.71e+06)
