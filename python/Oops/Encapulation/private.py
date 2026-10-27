class Student:
    def __init__(self, name,  age):
        self.__name = name # private variable
        self.__age = age          # private variable

    def display(self):
        print("Name:", self.__name) # Accessing private variable
        print("Age:", self.__age) # Accessing private variable

s1 = Student("Goutham", 20)
s1.display()
#print(s1.__name) # error: 'Student' object has no TTRIBUTE '__name'