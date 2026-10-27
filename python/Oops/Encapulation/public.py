#encapsulation - public

class Student:
    def __init__(self, name, age):
        self.name = name   # public
        self.age = age     # public

class Duplicate(Student):
    def change_name(self, name):
        print("Name:", self.name) #Accessing Public variable
        self.name = name # Modfying public variable

obj = Duplicate("john" , 20)
print(obj.name) # Access public variable
obj.change_name("jane") 
print(obj.name) #Accessing public modfyied variable