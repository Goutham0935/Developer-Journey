# for i in range(1, 3):
#     for j in range(1, 4):
#         print("*", end=" ")
#     print()

#calculator
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice : ")

    if choice == '1':
        num = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num, "+", num2, "=", num + num2)

    elif choice == '2':
        num = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num, "-", num2, "=", num - num2)

    elif choice == '3':
        num = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num, "*", num2, "=", num * num2)

    elif choice == '4':
        num = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        print(num, "/", num2, "=", num / num2)

    elif choice == '5':
        break
    else:
       print("invalid choice")