#Задание 1

class BasketballPlayersDatabase:
    def __init__(self):
        self.players = {}

    def add_player(self, name, height):
        self.players[name] = height
        print(f"{name} добавлен в базу данных.")

    def remove_player(self, name):
        if name in self.players:
            del self.players[name]
            print(f"{name} удален из базы данных.")
        else:
            print(f"{name} не найден в базе данных.")

    def search_player(self, name):
        if name in self.players:
            print(f"{name}: {self.players[name]} см")
        else:
            print(f"{name} не найден в базе данных.")

    def update_player(self, name, new_height):
        if name in self.players:
            self.players[name] = new_height
            print(f"Информация о росте {name} обновлена.")
        else:
            print(f"{name} не найден в базе данных.")

    def display_all_players(self):
        print("Список баскетболистов:")
        for name, height in self.players.items():
            print(f"{name}: {height} см")


# Пример использования программы
database = BasketballPlayersDatabase()

database.add_player("Леброн Джеймс", 203)
database.add_player("Коби Брайант", 198)
database.add_player("Майкл Джордан", 198)

database.display_all_players()

database.search_player("Леброн Джеймс")

database.update_player("Леброн Джеймс", 206)
database.search_player("Леброн Джеймс")

database.remove_player("Коби Брайант")

database.display_all_players()

#Задание 2

class EnglishFrenchDictionary:
    def __init__(self):
        self.dictionary = {}

    def add_word(self, english_word, french_translation):
        self.dictionary[english_word] = french_translation
        print(f"{english_word} добавлен в словарь.")

    def remove_word(self, english_word):
        if english_word in self.dictionary:
            del self.dictionary[english_word]
            print(f"{english_word} удален из словаря.")
        else:
            print(f"{english_word} не найден в словаре.")

    def search_translation(self, english_word):
        if english_word in self.dictionary:
            print(f"{english_word}: {self.dictionary[english_word]}")
        else:
            print(f"{english_word} не найден в словаре.")

    def update_translation(self, english_word, new_french_translation):
        if english_word in self.dictionary:
            self.dictionary[english_word] = new_french_translation
            print(f"Перевод для {english_word} обновлен.")
        else:
            print(f"{english_word} не найден в словаре.")

    def display_all_words(self):
        print("Словарь:")
        for english_word, french_translation in self.dictionary.items():
            print(f"{english_word}: {french_translation}")


# Пример использования программы
dictionary = EnglishFrenchDictionary()

dictionary.add_word("hello", "bonjour")
dictionary.add_word("apple", "pomme")
dictionary.add_word("cat", "chat")

dictionary.display_all_words()

dictionary.search_translation("hello")

dictionary.update_translation("hello", "salut")
dictionary.search_translation("hello")

dictionary.remove_word("apple")

dictionary.display_all_words()


#Задание 3
class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, full_name, phone, email, position, office_number, skype):
        self.employees[full_name] = {
            'Phone': phone,
            'Email': email,
            'Position': position,
            'Office Number': office_number,
            'Skype': skype
        }
        print(f"{full_name} добавлен в базу данных.")

    def remove_employee(self, full_name):
        if full_name in self.employees:
            del self.employees[full_name]
            print(f"{full_name} удален из базы данных.")
        else:
            print(f"{full_name} не найден в базе данных.")

    def search_employee(self, full_name):
        if full_name in self.employees:
            print(f"Информация о {full_name}:")
            for key, value in self.employees[full_name].items():
                print(f"{key}: {value}")
        else:
            print(f"{full_name} не найден в базе данных.")

    def update_employee(self, full_name, attribute, new_value):
        if full_name in self.employees and attribute in self.employees[full_name]:
            self.employees[full_name][attribute] = new_value
            print(f"{attribute} для {full_name} обновлен.")
        else:
            print(f"{full_name} или {attribute} не найдены в базе данных.")

    def display_all_employees(self):
        print("Список сотрудников:")
        for full_name, info in self.employees.items():
            print(f"{full_name}: {info}")


# Пример использования программы
firm = Company()

firm.add_employee("Иван Иванов", "123-456-7890", "ivan@example.com", "Программист", 101, "ivan.skype")
firm.add_employee("Мария Петрова", "987-654-3210", "maria@example.com", "Дизайнер", 202, "maria.skype")
firm.add_employee("Петр Сидоров", "555-123-4567", "petr@example.com", "Менеджер", 303, "petr.skype")

firm.display_all_employees()

firm.search_employee("Иван Иванов")

firm.update_employee("Иван Иванов", "Phone", "999-999-9999")
firm.search_employee("Иван Иванов")

firm.remove_employee("Мария Петрова")

firm.display_all_employees()


#Задание 4

class BookCollection:
    def __init__(self):
        self.books = {}

    def add_book(self, author, title, genre, year, pages, publisher):
        book_key = f"{author} - {title}"
        self.books[book_key] = {
            'Author': author,
            'Title': title,
            'Genre': genre,
            'Year': year,
            'Pages': pages,
            'Publisher': publisher
        }
        print(f"Книга '{title}' добавлена в коллекцию.")

    def remove_book(self, author, title):
        book_key = f"{author} - {title}"
        if book_key in self.books:
            del self.books[book_key]
            print(f"Книга '{title}' удалена из коллекции.")
        else:
            print(f"Книга '{title}' не найдена в коллекции.")

    def search_book(self, author, title):
        book_key = f"{author} - {title}"
        if book_key in self.books:
            print(f"Информация о книге '{title}':")
            for key, value in self.books[book_key].items():
                print(f"{key}: {value}")
        else:
            print(f"Книга '{title}' не найдена в коллекции.")

    def update_book(self, author, title, attribute, new_value):
        book_key = f"{author} - {title}"
        if book_key in self.books and attribute in self.books[book_key]:
            self.books[book_key][attribute] = new_value
            print(f"{attribute} для книги '{title}' обновлен.")
        else:
            print(f"Книга '{title}' или {attribute} не найдены в коллекции.")

    def display_all_books(self):
        print("Список книг в коллекции:")
        for book_key, info in self.books.items():
            print(f"{book_key}: {info}")


# Пример использования программы
collection = BookCollection()

collection.add_book("Агата Кристи", "Десять негритят", "Детектив", 1939, 300, "Издательство A")
collection.add_book("Лев Толстой", "Война и мир", "Роман", 1869, 1200, "Издательство B")
collection.add_book("Дж. Р. Р. Толкин", "Властелин колец", "Фэнтези", 1954, 500, "Издательство C")

collection.display_all_books()

collection.search_book("Агата Кристи", "Десять негритят")

collection.update_book("Агата Кристи", "Десять негритят", "Pages", 320)
collection.search_book("Агата Кристи", "Десять негритят")

collection.remove_book("Лев Толстой", "Война и мир")

collection.display_all_books()
