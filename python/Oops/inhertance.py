class Parent:
    def displayA(self):
        print("Parent Class")

class Child(Parent):
    def displayB(self):
        print("Child Class")

obj = Child()
obj.displayA()  # Accessing parent method      
obj.displayB()  # Accessing own method     