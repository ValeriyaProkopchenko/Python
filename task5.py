mass = float(input("Введите массу объекта в килограммах: "))
velocity = float(input("Введите скорость объекта в метрах в секунду: "))
kinetic_energy = 0.5 * mass * velocity ** 2
print(f"Кинетическая энергия: {kinetic_energy:.2f} Дж.")