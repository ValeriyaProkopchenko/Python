mass = float(input("Введите массу в кг: "))
c = float(input("Введите удельную теплоёмкость в Дж/(кг·°C): "))
delta_t = float(input("Введите изменение температуры в °C: "))
Q = mass * с * delta_t
print(f"Количество теплоты: {Q:.2f} Дж.")
