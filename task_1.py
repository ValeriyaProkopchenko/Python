distance = float(input("Введите расстояние в километрах: "))
time = float(input("Введите время в часах: "))
if time <= 0:
    print("Время должно быть больше нуля.")
else:
    speed = distance / time
    print(f"Скорость: {speed:.2f} км/ч.")
