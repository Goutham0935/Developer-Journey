## map()

#example of map():


numbers = [1, 5, 9, 3, 6]
squares = map(lambda x: x*x, numbers)
print(squares) # <map object at 0x00000238E1C78CC0> 
print(list(squares)) #[1, 25, 81, 9, 36]


## filter()

#example of filter():
nos  = [11, 15, 19, 13, 16]
squared_nos = filter(lambda x: x > 200, nos)
print(list(squared_nos)) #[]


##reduce():

#example of reduce():

from functools import reduce
nos = [21, 15, 19, 15, 16]
squared_nos  = reduce(lambda x, y: x + y, nos)
print(squared_nos)  # 86


#