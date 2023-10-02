#Задание 1: Сортировка списка

def sort_list(lst):
    average = sum(lst) / len(lst)
    
    if average > 0:
        first_two_thirds = sorted(lst[:int(2/3 * len(lst))])
        rest = lst[int(2/3 * len(lst)):]
    else:
        first_two_thirds = sorted(lst[:int(1/3 * len(lst))])
        rest = lst[int(1/3 * len(lst)):]
        rest.reverse()

    result = first_two_thirds + rest
    return result

my_list = [5, -2, 8, 3, 1, 0, -4, 7]
sorted_list = sort_list(my_list)
print("Отсортированный список:", sorted_list)

#Задание 2: Программа "Успеваемость"

def display_grades(grades):
    print("Оценки студента:", grades)

def retake_exam(grades):
    index = int(input("Введите номер оценки для пересдачи: ")) - 1
    new_grade = int(input("Введите новую оценку: "))
    grades[index] = new_grade
    print("Оценка успешно изменена.")

def scholarship(grades):
    average_grade = sum(grades) / len(grades)
    if average_grade >= 10.7:
        print("Студент имеет право на стипендию.")
    else:
        print("Студент не имеет права на стипендию.")

def sort_grades(grades, reverse=False):
    sorted_grades = sorted(grades, reverse=reverse)
    print("Отсортированные оценки:", sorted_grades)

grades_list = [9, 8, 10, 7, 12, 11, 9, 8, 10, 11]

while True:
    print("\nМеню:")
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Выходит ли стипендия")
    print("4. Вывод отсортированного списка оценок")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == '1':
        display_grades(grades_list)
    elif choice == '2':
        retake_exam(grades_list)
    elif choice == '3':
        scholarship(grades_list)
    elif choice == '4':
        order = input("Введите порядок сортировки (возрастание/убывание): ")
        if order.lower() == 'возрастание':
            sort_grades(grades_list)
        elif order.lower() == 'убывание':
            sort_grades(grades_list, reverse=True)
        else:
            print("Некорректный порядок сортировки.")
    elif choice == '0':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

    #Задание 3: Сортировка пузырьком с оптимизацией

 def bubble_sort_optimized(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

# Пример использования
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort_optimized(unsorted_list)
print("Отсортированный список:", sorted_list)