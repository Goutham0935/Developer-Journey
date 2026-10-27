# 1. Factorial (Direct Recursion)

def factorial(n):
    if n ==0 or  n == 1:
        return 1
    else:
        return n * factorial(n-1) # factorial 
    
print(factorial(8)) # 40320 


# 2. Fibonacci Series
def fibonacci(n):
    if  n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # fibonacci series
    
print(fibonacci(6)) # 8

# 3. Sum of Digits
def sum_digits(n):
    if n == 0:  
        return 0
    else:
        return n % 10 + sum_digits(n // 10)

print(sum_digits(1234))  # Output: 10