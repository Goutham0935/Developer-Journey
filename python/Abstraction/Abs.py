from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstracrt Class
    @abstractmethod
    def start(self): # Abstract method
        pass


class Car(Vehicle):   # Child class
    def start(self):  #Overriding abstract method
        print("Car started")

class Bike(Vehicle):  # Child class
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


c = Car()
b = Bike()
c.start()
b.start()
b.stop()