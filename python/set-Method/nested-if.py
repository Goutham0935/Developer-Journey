age = int(input("Enter Your age: "))
if age >= 18:
    drive = input("Can You Drive? (yes/no): ")
    if drive.lower() == "yes":
        print("You are eligible to drive.")
    else:
        print("You don't have a driver's license.")
else:
    print("You are not eligible for get a driver's license.")