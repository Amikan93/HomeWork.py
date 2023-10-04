#Задание 1: Класс Circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

# Пример использования
circle1 = Circle(5)
circle2 = Circle(7)

print(circle1 == circle2)  # Проверка на равенство радиусов
print(circle1 > circle2)   # Сравнение длин
print(circle1 + 2)         # Пропорциональное изменение размеров
print(circle2 - 1)
circle1 += 3
print(circle1.radius)

#Задание 2: Класс Complex

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_part, imag_part)

# Пример использования
complex1 = Complex(3, 4)
complex2 = Complex(1, 2)

result_add = complex1 + complex2
result_sub = complex1 - complex2
result_mul = complex1 * complex2
result_div = complex1 / complex2

print(result_add.real, "+", result_add.imag, "i")  # 4 + 6i
print(result_sub.real, "+", result_sub.imag, "i")  # 2 + 2i
print(result_mul.real, "+", result_mul.imag, "i")  # -5 + 10i
print(result_div.real, "+", result_div.imag, "i")  # 2 + 0i

#Задание 3: Класс Airplane

class Airplane:
    def __init__(self, plane_type, max_passengers):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __add__(self, passengers):
        return Airplane(self.plane_type, self.max_passengers + passengers)

    def __sub__(self, passengers):
        return Airplane(self.plane_type, max(0, self.max_passengers - passengers))

    def __iadd__(self, passengers):
        self.max_passengers += passengers
        return self

    def __isub__(self, passengers):
        self.max_passengers = max(0, self.max_passengers - passengers)
        return self

# Пример использования
plane1 = Airplane("Boeing 747", 500)
plane2 = Airplane("Airbus A380", 600)

print(plane1 == plane2)  # Проверка на равенство типов
print(plane1 > plane2)   # Сравнение по максимальному количеству пассажиров
print(plane1 + 100)      # Увеличение пассажиров
print(plane2 - 50)       # Уменьшение пассажиров
plane1 += 50
print(plane1.max_passengers)

#Задание 4: Класс Flat

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

# Пример использования
flat1 = Flat(80, 100000)
flat2 = Flat(70, 90000)

print(flat1 == flat2)  # Проверка на равенство площадей
print(flat1 != flat2)  # Проверка на неравенство площадей
print(flat1 > flat2)   # Сравнение по цене
print(flat1 < flat2)
print(flat1 >= flat2)