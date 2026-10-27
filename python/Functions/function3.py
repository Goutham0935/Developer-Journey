# Function Calling Another Function
def greet(name):
    return "helooo " + name

def welcome(name):
    print(greet(name))
    print("Welcome to our program")

welcome("Goutham")    


