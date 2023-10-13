import os
import pandas as pd
from datetime import datetime

class ToDoList:
    def __init__(self, file_path="tasks.xlsx"):
        """
        Инициализация ToDoList.

        Parameters:
        - file_path (str): Путь к файлу Excel, в котором будут храниться задачи.
        """
        self.file_path = file_path
        self.tasks = pd.DataFrame(columns=["Task", "Date"])

    def load_tasks(self):
        """
        Загрузка задач из Excel файла.
        """
        if os.path.exists(self.file_path):
            self.tasks = pd.read_excel(self.file_path)

    def save_tasks(self):
        """
        Сохранение задач в Excel файл.
        """
        self.tasks.to_excel(self.file_path, index=False)

    def add_task(self, task):
        """
        Добавление новой задачи в список.

        Parameters:
        - task (str): Текст задачи.
        """
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks = self.tasks.append({"Task": task, "Date": date_str}, ignore_index=True)

    def display_tasks(self):
        """
        Вывод списка задач на экран.
        """
        print("Список задач:")
        print(self.tasks)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ToDoList with Excel storage.")
    parser.add_argument("file_path", nargs="?", default="tasks.xlsx", help="Path to the Excel file.")
    args = parser.parse_args()

    todo_list = ToDoList(file_path=args.file_path)
    todo_list.load_tasks()

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Вывести список задач")
        print("3. Сохранить и выйти")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            task = input("Введите текст задачи: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            todo_list.save_tasks()
            print("Задачи сохранены. Программа завершена.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
