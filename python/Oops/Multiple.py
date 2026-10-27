class Father:
    def money(self):
        print("Father has money")

class Mother:
    def care(self):
        print("Mother has care")

class Child(Father, Mother):
    def love(self):
        print("Child has love")

obj = Child()
obj.money()
obj.care()
obj.love()
