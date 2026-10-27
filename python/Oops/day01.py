class Student:
    school = "ABC School"  # Class Variable

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    @classmethod
    def print_school(cls):
        return cls.school  # Accessing class variable

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school  # Modifying class variable


s1 = Student("Rahul", 101)
print(s1.print_school())

Student.change_school("XYZ School")
print(s1.print_school())