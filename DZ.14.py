# Задание 1

numbers = []

while True:
    print("\nМеню:")
    print("1. Добавить новое число в список")
    print("2. Удалить все вхождения числа из списка")
    print("3. Показать содержимое списка")
    print("4. Проверить есть ли значение в списке")
    print("5. Заменить значение в списке")
    print("0. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '0':
        break
    elif choice == '1':
        num = int(input("Введите число: "))
        if num in numbers:
            print("Число уже существует в списке.")
        else:
            numbers.append(num)
            print("Число добавлено в список.")
    elif choice == '2':
        num = int(input("Введите число для удаления: "))
        numbers = [x for x in numbers if x != num]
        print("Все вхождения числа удалены из списка.")
    elif choice == '3':
        direction = input("Показать список (1 - с начала, 2 - с конца): ")
        if direction == '1':
            print("Содержимое списка:", numbers)
        elif direction == '2':
            print("Содержимое списка:", numbers[::-1])
    elif choice == '4':
        num = int(input("Введите число для проверки: "))
        if num in numbers:
            print("Число есть в списке.")
        else:
            print("Числа нет в списке.")
    elif choice == '5':
        num = int(input("Введите число для замены: "))
        new_num = int(input("Введите новое число: "))
        replace_all = input("Заменить все вхождения? (y/n): ")
        if replace_all.lower() == 'y':
            numbers = [new_num if x == num else x for x in numbers]
        else:
            if num in numbers:
                index = numbers.index(num)
                numbers[index] = new_num
                print("Первое вхождение числа заменено.")
            else:
                print("Число не найдено в списке.")

# Задание 2

class StringStack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, string):
        if len(self.stack) < self.max_size:
            self.stack.append(string)
            print("Строка добавлена в стек.")
        else:
            print("Стек полон. Нельзя добавить новую строку.")

    def pop(self):
        if not self.is_empty():
            popped_string = self.stack.pop()
            print("Строка выталкивается из стека:", popped_string)
        else:
            print("Стек пуст. Нельзя вытолкнуть строку.")

    def count_strings(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size

    def clear_stack(self):
        self.stack = []
        print("Стек очищен.")

    def peek(self):
        if not self.is_empty():
            print("Верхняя строка в стеке:", self.stack[-1])
        else:
            print("Стек пуст. Нет верхней строки.")

# Пример использования
stack = StringStack(3)

while True:
    print("\nМеню:")
    print("1. Поместить строку в стек")
    print("2. Вытолкнуть строку из стека")
    print("3. Подсчет количества строк в стеке")
    print("4. Проверка пустоты стека")
    print("5. Проверка полноты стека")
    print("6. Очистить стек")
    print("7. Получить значение без выталкивания")
    print("0. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '0':
        break
    elif choice == '1':
        string = input("Введите строку: ")
        stack.push(string)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        print("Количество строк в стеке:", stack.count_strings())
    elif choice == '4':
        print("Стек пуст:", stack.is_empty())
    elif choice == '5':
        print("Стек полон:", stack.is_full())
    elif choice == '6':
        stack.clear_stack()
    elif choice == '7':
        stack.peek()


# Задание 3

class StringStack:
    def __init__(self):
        self.stack = []

    def push(self, string):
        self.stack.append(string)
        print("Строка добавлена в стек.")

    def pop(self):
        if not self.is_empty():
            popped_string = self.stack.pop()
            print("Строка выталкивается из стека:", popped_string)
        else:
            print("Стек пуст. Нельзя вытолкнуть строку.")

    def count_strings(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def clear_stack(self):
        self.stack = []
        print("Стек очищен.")

    def peek(self):
        if not self.is_empty():
            print("Верхняя строка в стеке:", self.stack[-1])
        else:
            print("Стек пуст. Нет верхней строки.")

# Пример использования
stack = StringStack()

while True:
    print("\nМеню:")
    print("1. Поместить строку в стек")
    print("2. Вытолкнуть строку из стека")
    print("3. Подсчет количества строк в стеке")
    print("4. Проверка пустоты стека")
    print("5. Очистить стек")
    print("6. Получить значение без выталкивания")
    print("0. Выход")

    choice = input("Выберите пункт меню: ")

    if choice == '0':
        break
    elif choice == '1':
        string = input("Введите строку: ")
        stack.push(string)
    elif choice == '2':
        stack.pop()
    elif choice == '3':
        print("Количество строк в стеке:", stack.count_strings())
    elif choice == '4':
        print("Стек пуст:", stack.is_empty())
    elif choice == '5':
        stack.clear_stack()