import math
import pickle

class Shape:
    def show(self):
        pass

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Square at ({self.x}, {self.y}) with side length {self.side_length}")

class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")

class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Ellipse at ({self.x}, {self.y}) with width {self.width} and height {self.height}")


# Пример использования классов и сохранение/загрузка в файл
shapes = [
    Square(0, 0, 5),
    Rectangle(2, 3, 4, 6),
    Circle(1, 1, 3),
    Ellipse(5, 5, 4, 2)
]

# Сохранение в файл
for idx, shape in enumerate(shapes):
    shape.save(f'shape_{idx}.pkl')

# Загрузка из файла
loaded_shapes = [Shape.load(f'shape_{idx}.pkl') for idx in range(len(shapes))]

# Вывод информации о фигурах
for shape in loaded_shapes:
    shape.show()
