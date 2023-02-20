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


def noise(x, y):
    # применяем хэш-функцию к координатам
    h = hash((x, y))
    # используем полученное число для создания шума
    noise_val = (h % 10000) / 10000.0
    # применяем к шуму некоторые преобразования для улучшения качества
    noise_val = 0.5 + 0.5 * math.sin(noise_val * 2 * math.pi * 10)
    return noise_val, noise_val, noise_val


def val_noise(x, y, octaves=6, persistence=300, lacunarity=.05):
    total = 0.0
    frequency = 1.0
    amplitude = 1.0
    max_val = 0.0
    for i in range(octaves):
        val = noise(x * frequency, y * frequency)
        total += val[0] * amplitude
        max_val += amplitude
        amplitude *= persistence
        frequency *= lacunarity
    return total / max_val, total / max_val, total / max_val


# def fractal_noise(x, y, octaves=5, persistence=0.5, lacunarity=2.0):
#     amplitude = 1.0
#     frequency = 1.0
#     noise_val = 0.0
#
#     for i in range(octaves):
#         octave_val = val_noise(x * frequency, y * frequency)[0]
#         noise_val += octave_val * amplitude
#         amplitude *= persistence
#         frequency *= lacunarity
#
#     return noise_val, 0.8, 1.0
#
# def func(x, y, octaves=1, lacunarity=2, persistence=0.5):
#     frequency = 1
#     amplitude = 1
#     total = 0
#     for i in range(octaves):
#         total += val_noise(x * frequency, y * frequency)[0] * amplitude
#         frequency *= lacunarity
#         amplitude *= persistence
#     return total, 0.8, 1

def func(x, y):
    cloud_noise = 1
    for octave in range(8):
        scale = 20 ** octave
        cloud_noise += val_noise(x * scale, y * scale)[0] * (1 / scale)
    cloud_noise = cloud_noise * 0.5 + 0.5  # приводим значения к диапазону [0, 1]

    sky_color = (0.6, 0.8, 1.0)
    horizon_color = (0.0, 0.2, 0.4)
    sky_y = y * 3 - 1  # приводим y к диапазону [-1, 1]
    sky_color = tuple((a * (1 - sky_y) + b * (sky_y + 1)) / 2 for a, b in zip(sky_color, horizon_color))

    sky_noise = val_noise(x * 2, y * 0.2)[0] * 0.1  # добавляем небольшой шум к цвету неба

    # комбинируем цвет неба и облаков
    color = tuple((c * (1 - cloud_noise) + sky_color[i] * cloud_noise) * (1 - sky_noise) for i, c in enumerate(sky_color))

    return color


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
