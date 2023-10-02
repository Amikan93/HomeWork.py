#Задание 1: Форматированный текст

def display_quote():
    quote = """Don't let the noise of others' opinions
drown out your own inner voice."""
    author = "Steve Jobs"
    print(quote)
    print(author)

display_quote()

#Задание 2: Нечетные числа между двумя числами

def display_odd_numbers(start, end):
    odd_numbers = [num for num in range(start, end + 1) if num % 2 != 0]
    print("Нечетные числа между", start, "и", end, ":", odd_numbers)

display_odd_numbers(3, 12)

#Задание 3: Горизонтальная или вертикальная линия

def display_line(length, direction, symbol):
    if direction == 'горизонтальная':
        print(symbol * length)
    elif direction == 'вертикальная':
        for _ in range(length):
            print(symbol)

display_line(5, 'горизонтальная', '*')

#Задание 4: Максимальное из четырех чисел

def max_of_four(a, b, c, d):
    return max(a, b, c, d)

result = max_of_four(10, 5, 8, 20)
print("Максимальное число из четырех:", result)

#Задание 5: Сумма чисел в диапазоне

def sum_in_range(start, end):
    return sum(range(start, end + 1))

result = sum_in_range(1, 5)
print("Сумма чисел в диапазоне:", result)

#Задание 6: Проверка на простое число

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

result = is_prime(7)
print("Число простое?", result)

#Задание 7: Проверка на счастливое шестизначное число

def is_happy_number(number):
    digits = [int(digit) for digit in str(number)]
    if len(digits) != 6:
        return False
    return sum(digits[:3]) == sum(digits[3:])

result = is_happy_number(123420)
print("Счастливое шестизначное число?", result)