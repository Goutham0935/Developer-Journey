while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    try:
        choice = int(input("Enter choice (1/2/3/4/5): "))
    except ValueError:
        print("Invalid choice. Program ends here.")
        break
    else:
        if choice == 5:
            print("Goodbye!")
            break

        if choice not in (1, 2, 3, 4):
            print("Invalid choice. Program ends here.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only. Program ends here.")
            break
        else:
            try:
                if choice == 1:
                    result = num1 + num2
                elif choice == 2:
                    result = num1 - num2
                elif choice == 3:
                    result = num1 * num2
                elif choice == 4:
                    if num2 == 0:
                        raise ZeroDivisionError
                    result = num1 / num2
            except ZeroDivisionError:
                print("Error: Cannot divide by zero. Program ends here.")
                break
            else:
                print(f"Result: {result}")
            finally:
                print("Calculation finished.")
