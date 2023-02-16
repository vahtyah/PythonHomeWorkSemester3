import math


def main(n, a, m, y):
    f1 = sum(sum(c**2 - 41*math.log(j**2+23)**3 for c in range(1, n + 1)) for j in range(1, a + 1))
    f2 = 1
    for i in range(1, n + 1):
        f2 *= sum(sum(17*(93*j**3)**2-78-(abs(y**2-i**3-k))**4 for k in range(1, a + 1)) for j in range(1, m + 1))
    return f1 - f2


print(main(6, 8, 5, 0.46))
print(2.96e+62)
