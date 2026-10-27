## Lambda function

#normal function

def circle(x):
    return 3.14 * x * x
print(circle(5))  # 78.5


# Single Argument:

Circle = lambda x: 3.14 * x * x
print(Circle(10)) # 314.0


#multiple Arguments:

add = lambda a, b: a + b
print(add(8, 10)) # 18


#no Arguments:

greet = lambda: "Hello, World"
print(greet()) # "Hello, World"


#Real-Life Example:

# Calculate discount price
discount_price = lambda price, discount: price - (price * discount/100)
print(discount_price(500, 10)) # 450.0

