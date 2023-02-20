import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
import hashlib

def noise_gradient(x, y):
    """Градиентный шум."""
    def fade(t):
        return t * t * t * (t * (t * 6 - 15) + 10)

    def lerp(t, a, b):
        return a + t * (b - a)

    def grad(hash, x, y):
        h = hash & 3
        if h == 0:
            return x + y
        elif h == 1:
            return -x + y
        elif h == 2:
            return x - y
        else:
            return -x - y

    xi = int(x) & 255
    yi = int(y) & 255
    xf = x - int(x)
    yf = y - int(y)
    u = fade(xf)
    v = fade(yf)
    a = hash_table[hash_table[xi] + yi]
    b = hash_table[hash_table[xi + 1] + yi]
    c = hash_table[hash_table[xi] + yi + 1]
    d = hash_table[hash_table[xi + 1] + yi + 1]
    x1 = lerp(u, grad(a, xf, yf), grad(b, xf - 1, yf))
    x2 = lerp(u, grad(c, xf, yf - 1), grad(d, xf - 1, yf - 1))
    return (lerp(v, x1, x2) + 1) / 2

def fractal_noise(x, y, octaves, persistence):
    """Фрактальный шум на основе градиентного шума."""
    amplitude = 1
    frequency = 1
    noise_value = 0
    for i in range(octaves):
        noise_value += noise_gradient(x * frequency, y * frequency) * amplitude
        amplitude *= persistence
        frequency *= 2
    return noise_value

def func(x, y):
    """Функция для создания облаков на основе фрактального шума."""
    value = fractal_noise(x, y, octaves=4, persistence=0.5)
    value = math.pow(value, 3)
    return (value, value, value)


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
