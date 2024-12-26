import math
radius = float(input("Введите радиус основания цилиндра в метрах: "))
height = float(input("Введите высоту цилиндра в метрах: "))
volume = math.pi * radius ** 2 * height
print(f"Объем цилиндра: {volume:.2f} м^3.")