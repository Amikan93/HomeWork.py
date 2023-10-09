
#Задание 1
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"{self.brand} {self.model}")

class CoffeeMachine(Device):
    def __init__(self, brand, model, coffee_type):
        super().__init__(brand, model)
        self.coffee_type = coffee_type

    def make_coffee(self):
        print(f"Making {self.coffee_type} coffee")

class Blender(Device):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def blend(self):
        print(f"Blending at speed {self.speed}")

class MeatGrinder(Device):
    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print(f"Grinding meat with {self.power} power")


# Задание 2
class Ship:
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    def sail(self):
        print(f"{self.name} is sailing")

class Frigate(Ship):
    def __init__(self, name, displacement, num_cannons):
        super().__init__(name, displacement)
        self.num_cannons = num_cannons

    def fire_cannons(self):
        print(f"{self.name} fires {self.num_cannons} cannons")

class Destroyer(Ship):
    def __init__(self, name, displacement, missile_system):
        super().__init__(name, displacement)
        self.missile_system = missile_system

    def launch_missiles(self):
        print(f"{self.name} launches missiles with {self.missile_system}")

class Cruiser(Ship):
    def __init__(self, name, displacement, radar_type):
        super().__init__(name, displacement)
        self.radar_type = radar_type

    def use_radar(self):
        print(f"{self.name} is using radar of type {self.radar_type}")


# Задание 3
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def display(self):
        print(f"${self.dollars}.{self.cents}")

    def set_money(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

# Пример использования
money = Money(10, 50)
money.display()

money.set_money(20, 75)
money.display()