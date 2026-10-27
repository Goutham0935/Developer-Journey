print("Hello, World!")  
print(5 + 3)
print("Hello, World!", 5 + 3, sep=" | ", end=" | ")

# Printing Multiple Values
name = "Jenish"
age = 20
print("Name:", name, "Age:", age)

# Using sep Parameter
print("Python", "is", "fun", sep="-")

# Using end Parameter
print("Hello", end=" ")
print("World")

# Printing with f-strings / Formatting
name = "Jenish"
age = 20
print(f"My name is {name} and I am {age} years old.")

# use .format()
print("My name is {} and I am {} years old.".format(name, age))

# Printing with Escape Sequences

# \n → new line
# \t → tab
# \\ → backslash
# \" → double quote

print("Hello\nWorld")  # Newline
print("A\tB")          # Tab space
print("Hello\\World")  # Backslash
print("Hello\"World")  # Double quote