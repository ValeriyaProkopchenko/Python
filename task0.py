def task_1():
  distance = float(input("Введите расстояние в километрах: "))
  time = float(input("Введите время в часах: "))
  if time <= 0:
    print("Время должно быть больше нуля.")
  else:
    speed = distance / time
    print(f"Скорость: {speed:.2f} км/ч.")

def task_2():
  force = float(input("Введите силу в ньютонах: "))
  acc = float(input("Введите ускорение в метрах на секунду в квадрате: "))
  if acc == 0:
    print("Ускорение не должно быть равно нулю.")
  else:
    mass = force / acc
    print(f"Масса: {mass:.2f} кг.")

def task_3():
  f = float(input("Введите температуру в градусах Фаренгейта: "))
  c = (f - 32) * 5 / 9
  print(f"Температура в градусах Цельсия: {c:.2f} °C.")

def task_4():
  force = float(input("Введите силу в ньютонах: "))
  distance = float(input("Введите расстояние в метрах: "))
  work = force * distance
  print(f"Работа: {work:.2f} Дж.")

def task_5():
  mass = float(input("Введите массу объекта в килограммах: "))
  velocity = float(input("Введите скорость объекта в метрах в секунду: "))
  kinetic_energy = 0.5 * mass * velocity ** 2
  print(f"Кинетическая энергия: {kinetic_energy:.2f} Дж.")

def task_6():
  mass = float(input("Введите массу в килограммах: "))
  height = float(input("Введите высоту в метрах: "))
  g = float(input("Введите значение ускорения свободного падения (м/с²): "))
  potential_energy = mass * g * height
  print(f"Потенциальная энергия: {potential_energy:.2f} Дж.")

def task_7():
  force = float(input("Введите силу в ньютонах: "))
  square = float(input("Введите площадь в квадратных метрах: "))
  if square <= 0:
    print(" Площадь должна быть больше нуля.")
  else:
    pressure = force / square
    print(f"Давление: {pressure:.2f} Па.")

def task_8():
  mass = float(input("Введите массу в кг: "))
  c = float(input("Введите удельную теплоёмкость в Дж/(кг·°C): "))
  delta_t = float(input("Введите изменение температуры в °C: "))
  Q = mass * с * delta_t
  print(f"Количество теплоты: {Q:.2f} Дж.")

def task_9():
  T = float(input("Введите период колебаний в секундах: "))
  V = 1 / T
  print(f"Частота: {V:.2f} Гц.")

def task_10():
  import math
  radius = float(input("Введите радиус основания цилиндра в метрах: "))
  height = float(input("Введите высоту цилиндра в метрах: "))
  volume = math.pi * radius ** 2 * height
  print(f"Объем цилиндра: {volume:.2f} м^3.")

def main():
  while True:
    print("\nВыберите задачу (1-10) или нажмите 'q' для выхода:")
    choice = input()

    if choice == 'q':
      break

    tasks = {
      '1': task_1,
      '2': task_2,
      '3': task_3,
      '4': task_4,
      '5': task_5,
      '6': task_6,
      '7': task_7,
      '8': task_8,
      '9': task_9,
      '10': task_10
    }

    if choice in tasks:
      tasks[choice]()
    else:
      print("Неверный выбор. Пожалуйста, выберите задачу от 1 до 10.")

if __name__ == "__main__":
  main()
