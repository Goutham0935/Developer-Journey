try:
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))
    div = num1/num2

except ZeroDivisionError:
    print("you got a error because you divided by 0")
except ValueError:
    print("You got a error because of  you did not enter a number")
    
else:
    print(div)
finally:
    print("finally")
print("thanks for using this program")

       