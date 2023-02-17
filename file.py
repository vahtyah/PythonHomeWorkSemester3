def main(z, x, y):
    a = ((3*z)**2 + (x**2 - 80*y - 69)**4)
    b = ((z**3-52*y-x**2)**5)
    c = (abs(z))**7 + 43*(x**2 + 60 + 49*y)**2
    return (a/b) + c

print(main(1,2,3))