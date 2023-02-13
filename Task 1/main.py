import math


def main(z, y, x):
    return (((59 * (z ** 2) - 33 * (y ** 3) - 94 * y) ** 2) + x) / ((97 * (x ** 2) + y + (z ** 3)) ** 6) + math.sqrt(
        (math.atan(z) ** 4) - (x / 33 - 3 * (y ** 3) - 96 * (x ** 2)) ** 3)


print(main(-0.56, 0.66, 0.72))
