from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AIRCONDITION_PER_KM = 0.9

    def drive(self, distance):
        fuel_for_distance = distance * Car.AIRCONDITION_PER_KM + distance * self.fuel_consumption
        if fuel_for_distance <= self.fuel_quantity:
            self.fuel_quantity -= fuel_for_distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIRCONDITION_PER_KM = 1.6

    def drive(self, distance):
        fuel_for_distance = distance * Truck.AIRCONDITION_PER_KM + distance * self.fuel_consumption
        if fuel_for_distance <= self.fuel_quantity:
            self.fuel_quantity -= fuel_for_distance

    def refuel(self, fuel):
        fuel = fuel * 0.95
        self.fuel_quantity += fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)