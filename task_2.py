force = float(input("Введите силу в ньютонах: "))
acc = float(input("Введите ускорение в метрах на секунду в квадрате: "))
if acc == 0:
    print("Ускорение не должно быть равно нулю.")
else:
    mass = force / acc
    print(f"Масса: {mass:.2f} кг.")
