class Parent:
    def display(self):
        print("Common parent")

class Child(Parent):
    def show1(self):
        print("Child 1 Class")

class Child2(Parent):
    def show2(self):
        print("Child 2 class")

obj1 = Child()
obj2 = Child2()

obj1.display()
obj1.show1()
obj2.display()
obj2.show2()
