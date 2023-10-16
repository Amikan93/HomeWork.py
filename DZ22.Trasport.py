class Vehicle:
    def __init__(self, vehicle_type):
        self.type = vehicle_type

    def get_type(self) -> str:
        return self.type

    def __repr__(self) -> str:
        return f"Vehicle(type={self.type})"

    def __str__(self) -> str:
        return f"Type: {self.type}"


class Bus(Vehicle):
    def __init__(self, number):
        super().__init__("Bus")
        self.number = number

    def get_number(self) -> str:
        return self.number

    def __repr__(self) -> str:
        return f"Bus(number={self.number})"

    def __str__(self) -> str:
        return f"Bus Number: {self.number}"


class BusSchedule:
    def __init__(self):
        self.schedule = []

    def add_bus(self, bus_number, departure_time):
        self.schedule.append((bus_number, departure_time))

    def get_schedule(self) -> list:
        return self.schedule

    def get_schedule_by_bus_number(self, bus_number) -> list:
        return [(bus, time) for bus, time in self.schedule if bus == bus_number]

    def is_bus(self, vehicle_number) -> bool:
        return any(bus == vehicle_number for bus, _ in self.schedule)

    def check_schedule(self, bus_number, departure_time) -> bool:
        return (bus_number, departure_time) in self.schedule


# Тесты
def run_tests():
    # Тесты для класса Vehicle
    vehicle = Vehicle("Car")
    assert vehicle.get_type() == "Car"
    assert repr(vehicle) == "Vehicle(type=Car)"
    assert str(vehicle) == "Type: Car"

    # Тесты для класса Bus
    bus = Bus("101")
    assert bus.get_type() == "Bus"
    assert bus.get_number() == "101"
    assert repr(bus) == "Bus(number=101)"
    assert str(bus) == "Bus Number: 101"

    # Тесты для класса BusSchedule
    schedule = BusSchedule()
    schedule.add_bus("101", "10:00")
    schedule.add_bus("102", "12:00")

    assert schedule.get_schedule() == [("101", "10:00"), ("102", "12:00")]
    assert schedule.get_schedule_by_bus_number("101") == [("101", "10:00")]
    assert schedule.is_bus("102") is True
    assert schedule.is_bus("103") is False
    assert schedule.check_schedule("101", "10:00") is True
    assert schedule.check_schedule("101", "12:00") is False

    print("All tests passed successfully.")


# Запуск тестов
run_tests()
