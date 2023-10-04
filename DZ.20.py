import re

class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.isalpha():
            raise ValueError("Name must contain only letters.")
        instance._name = value

class AgeDescriptor:
    def __get__(self, instance, owner):
        return instance._age

    def __set__(self, instance, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer.")
        instance._age = value

class EmailDescriptor:
    def __get__(self, instance, owner):
        return instance._email

    def __set__(self, instance, value):
        email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not re.match(email_pattern, value):
            raise ValueError("Invalid email format.")
        instance._email = value

class User:
    def __init__(self, name, age, email):
        self._name = name
        self._age = age
        self._email = email

    name = NameDescriptor()
    age = AgeDescriptor()
    email = EmailDescriptor()

class Database:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def update_user(self, old_user, new_user):
        index = self.users.index(old_user)
        self.users[index] = new_user

    def delete_user(self, user):
        self.users.remove(user)

    def find_users_by_name(self, name):
        return [user for user in self.users if user.name == name]

    def find_users_by_age(self, age):
        return [user for user in self.users if user.age == age]

    def find_users_by_email(self, email):
        return [user for user in self.users if user.email == email]

# Пример использования базы данных
db = Database()

# Добавление пользователей
user1 = User("Alice", 25, "alice@example.com")
user2 = User("Bob", 30, "bob@example.com")
db.add_user(user1)
db.add_user(user2)

# Поиск пользователей
found_users = db.find_users_by_name("Alice")
for user in found_users:
    print(f"Found user by name: {user.name}, age: {user.age}, email: {user.email}")

# Обновление пользователя
updated_user = User("Alice Smith", 26, "alice.smith@example.com")
db.update_user(user1, updated_user)

# Поиск пользователей по новым данным
found_users = db.find_users_by_name("Alice Smith")
for user in found_users:
    print(f"Found user by name: {user.name}, age: {user.age}, email: {user.email}")

# Удаление пользователя
db.delete_user(updated_user)
print("User deleted.")

# Поиск пользователей после удаления
found_users = db.find_users_by_name("Alice Smith")
print(f"Found {len(found_users)} users by name 'Alice Smith'")
