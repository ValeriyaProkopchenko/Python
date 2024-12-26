force = float(input("Введите силу в ньютонах: "))
square = float(input("Введите площадь в квадратных метрах: "))
if square <= 0:
    print(" Площадь должна быть больше нуля.")
else:
    pressure = force / square
    print(f"Давление: {pressure:.2f} Па.")