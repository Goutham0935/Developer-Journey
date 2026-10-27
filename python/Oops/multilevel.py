class GrandParent:
    def property(self):
        print("GrandParent has property")

class Parent(GrandParent):
    def money(self):
        print("Parent has money")

class Child(Parent):
    def car(self):
        print("child has car")

obj = Child()
obj.property()  #accessing Grandparent
obj.money()  # Acceessing Parent
obj.car()  # Accessing own method
