def main(y, z):
    n = len(y) - 1
    result = sum(((z[int(n + 1 - ((i / 2) // 1 + 1))]) ** 2 + y[int((i / 3) // 1 + 1)] + 58 * (y[int((i / 2) // 1 + 1)])
                  ** 3) ** 4 for i in range(1, n + 1))
    return result


print(main([0.94, -0.01, 0.22, -0.06, 0.35, 0.45, -0.27], [-0.17, -0.3, 0.52, -0.1, 0.68, 0.08, 0.13]))
