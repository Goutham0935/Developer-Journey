# Person with name and age
# ------------------------------

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# a = Person("Sasi", 21)
# b = Person("Rani", 20)

# print("Name:", a.name)
# print("age:", a.age)
# print("--------------------------------------------")

# print("Name:", b.name)
# print("age:", b.age)
# print("--------------------------------------------")


# Book Class
# ---------------

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("------------------------------------------------")

b1 = Book("The Psychology of Money", "Morgan Housel", 289 )
b2 = Book("Think Like a Monk", "Jay Shetty", 299 )
b1.display()
b2.display()