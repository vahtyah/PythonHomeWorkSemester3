import math


def main(x):
    if x < 36:
        return ((x**3+x**2)**7)/74-x**5-20*math.atan(x**2+50*x**3+38)**4
    elif 36 <= x < 125:
        return (6 * x ** 3) ** 7
    elif 125 <= x < 154:
        return 28 * x
    elif 154 <= x < 187:
        return 41*math.log(x**2+23)+20
    else:
        return 24 * x ** 2
