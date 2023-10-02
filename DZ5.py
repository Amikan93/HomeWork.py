#Задание 1 

def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print("Ошибка в выражении:", e)

user_expression = input("Введите арифметическое выражение: ")
result = calculate_expression(user_expression)

if result is not None:
    print("Результат выражения:", result)

#Задание 2

import random

# Создаем случайный список целых чисел
random_numbers = [random.randint(-10, 10) for _ in range(10)]

def analyze_numbers(numbers):
    min_number = min(numbers)
    max_number = max(numbers)
    negative_count = sum(1 for num in numbers if num < 0)
    positive_count = sum(1 for num in numbers if num > 0)
    zero_count = sum(1 for num in numbers if num == 0)

    print("Минимальный элемент:", min_number)
    print("Максимальный элемент:", max_number)
    print("Количество отрицательных элементов:", negative_count)
    print("Количество положительных элементов:", positive_count)
    print("Количество нулей:", zero_count)

print("Список случайных чисел:", random_numbers)
analyze_numbers(random_numbers)

