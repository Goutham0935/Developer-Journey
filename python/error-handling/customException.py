class DrivingError(Exception): #DrivingError(Exception) - self created error or customized error, pass - for skiping that error part.
    pass

age =  int(input("Enter your age: "))
if  age < 18:
    raise DrivingError("Age must be at least 18")

print("Thanks")