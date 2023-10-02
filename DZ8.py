def main():
    while True:
        print("Выберите программу:")
        print("1. Справочник")
        print("2. Книги")
        print("3. Выход")
        
        choice = input("Введите номер программы: ")

        if choice == "1":
            run_phonebook_program()
        elif choice == "2":
            run_books_program()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

def run_phonebook_program():
    ids = [101, 102, 103, 104]
    phones = ["555-1111", "555-2222", "555-3333", "555-4444"]

    while True:
        print("\nМеню справочника:")
        print("1. Отсортировать по идентификационным кодам")
        print("2. Отсортировать по номерам телефона")
        print("3. Вывести список пользователей с кодами и телефонами")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            sorted_ids, sorted_phones = sort_by_ids(ids, phones)
            print_phonebook(sorted_ids, sorted_phones)
        elif choice == "2":
            sorted_ids, sorted_phones = sort_by_phones(ids, phones)
            print_phonebook(sorted_ids, sorted_phones)
        elif choice == "3":
            print_phonebook(ids, phones)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")

def sort_by_ids(ids, phones):
    sorted_data = sorted(zip(ids, phones))
    sorted_ids, sorted_phones = zip(*sorted_data)
    return sorted_ids, sorted_phones

def sort_by_phones(ids, phones):
    sorted_data = sorted(zip(phones, ids))
    sorted_phones, sorted_ids = zip(*sorted_data)
    return sorted_ids, sorted_phones

def print_phonebook(ids, phones):
    print("\nСправочник:")
    for i in range(len(ids)):
        print(f"Код: {ids[i]}, Телефон: {phones[i]}")

def run_books_program():
    titles = ["Книга1", "Книга2", "Книга3", "Книга4"]
    years = [2000, 1998, 2010, 2005]

    while True:
        print("\nМеню книг:")
        print("1. Отсортировать по названию книг")
        print("2. Отсортировать по годам выпуска")
        print("3. Вывести список книг с названиями и годами выпуска")
        print("4. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            sorted_titles, sorted_years = sort_by_titles(titles, years)
            print_books(sorted_titles, sorted_years)
        elif choice == "2":
            sorted_titles, sorted_years = sort_by_years(titles, years)
            print_books(sorted_titles, sorted_years)
        elif choice == "3":
            print_books(titles, years)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите 1, 2, 3 или 4.")

def sort_by_titles(titles, years):
    sorted_data = sorted(zip(titles, years))
    sorted_titles, sorted_years = zip(*sorted_data)
    return sorted_titles, sorted_years

def sort_by_years(titles, years):
    sorted_data = sorted(zip(years, titles))
    sorted_years, sorted_titles = zip(*sorted_data)
    return sorted_titles, sorted_years

def print_books(titles, years):
    print("\nСписок книг:")
    for i in range(len(titles)):
        print(f"Название: {titles[i]}, Год выпуска: {years[i]}")

# Запуск программы
main()
