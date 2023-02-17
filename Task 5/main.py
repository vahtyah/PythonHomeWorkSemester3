import math


def main(y, z):
    return sum(((z[len(y) - math.ceil(i / 2)])
                ** 2 + y[math.ceil(i / 3) - 1] + 58 *
                (y[math.ceil(i / 2) - 1]) ** 3) ** 4
               for i in range(1, len(y) + 1))
