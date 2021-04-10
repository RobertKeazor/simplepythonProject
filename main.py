# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Vehicle:
    make = ""
    model = ""
    year = ""
    weight = 0

    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def display(self):
        print("hello " + self.make)


class Car(Vehicle):
    pass


car = Car("Telsa", "Model", "2020", 5000)
car.display()