import math


def main(n):
    if n == 0:
        return 0.21
    elif n >= 1:
        return 29*math.sin(main(n-1))**3 - 78 - 89 * (main(n-1)//1 + 1)


print(main(8))
print(9.22e+11)
