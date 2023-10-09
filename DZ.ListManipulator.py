#Задание 1

from typing import Any

class ListManipulator:
    def __init__(self, my_list: list):
        self._my_list = my_list

    def get_length(self) -> int:
        return len(self._my_list)

    def add_element(self, element: Any) -> None:
        self._my_list.append(element)

    def remove_element(self, element: Any) -> None:
        try:
            self._my_list.remove(element)
        except ValueError:
            raise ValueError(f"Element {element} not found in the list")

    def get_element_at_index(self, index: int) -> Any:
        try:
            return self._my_list[index]
        except IndexError:
            raise IndexError("Index out of range")

    @staticmethod
    def merge_lists(list1: list, list2: list) -> list:
        return list1 + list2
    

#Задание 2

class FileManager:
    def __init__(self, file_name: str):
        self._file_name = file_name

    def read_file(self) -> str:
        try:
            with open(self._file_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return "File not found"

    def write_to_file(self, content: str) -> None:
        with open(self._file_name, 'w') as file:
            file.write(content)

#Задание 3

from datetime import datetime, timedelta

class DateTimeManager:
    def __init__(self):
        self.current_date_time = datetime.now()

    def add_days(self, days: int) -> None:
        self.current_date_time += timedelta(days=days)

    def subtract_days(self, days: int) -> None:
        self.current_date_time -= timedelta(days=days)

    def format_date(self, format_string: str) -> str:
        return self.current_date_time.strftime(format_string)
    
# Задание 1
list_manipulator = ListManipulator([1, 2, 3])
list_manipulator.add_element(4)
list_manipulator.remove_element(2)
print(list_manipulator.get_length())
print(list_manipulator.get_element_at_index(1))
print(ListManipulator.merge_lists([1, 2], [3, 4]))

# Задание 2
file_manager = FileManager("example.txt")
file_manager.write_to_file("Hello, World!")
print(file_manager.read_file())

# Задание 3
date_time_manager = DateTimeManager()
date_time_manager.add_days(5)
date_time_manager.subtract_days(2)
print(date_time_manager.format_date("%Y-%m-%d %H:%M:%S"))