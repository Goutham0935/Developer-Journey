try:
    x = int("abc")
except ZeroDivisionError as e:
    print("cannot divided by zero")  

except Exception as e: #Exception is a basic class all exception
    print(type(e).__name__,":",e)

print("thanks")       