mass = float(input("Введите массу в килограммах: "))
height = float(input("Введите высоту в метрах: "))
g = float(input("Введите значение ускорения свободного падения (м/с²): "))
potential_energy = mass * g * height
print(f"Потенциальная энергия: {potential_energy:.2f} Дж.")