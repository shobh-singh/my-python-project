class Vehicle:
    def info_vehicle(self):
        print("Vehicle class")

class Car(Vehicle):
    def info_car(self):
        print("Car class")

class Bike(Vehicle):
    def info_bike(self):
        print("Bike class")

c = Car()
b = Bike()
c.info_vehicle()
c.info_car()
b.info_vehicle()
b.info_bike()
