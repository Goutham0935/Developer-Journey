# Q. Write a program that reads student marks from input. Raise custom exceptions if marks are negative or greater than 100.

class NegativeError(Exception):
    pass

class GreaterError(Exception):
    pass


try:
    marks = int(input("Enter your mark: "))

    if marks < 0:
        raise NegativeError("Marks cannot be negative.")

    if marks > 100:
        raise GreaterError("Marks cannot be more than 100 ")
    
    print("student marks :", marks)

except NegativeError as e:
    print("Error:", e)

except GreaterError as e:
    print("Error:", e)