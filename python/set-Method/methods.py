# add
num = {5,6,7,}
num.add(8)
print(num)
print("--------------------------------------------------")

#clear
num.clear()
print(num)
print("--------------------------------------------------")


#discord
name={"John", "Doe", "Jane"}
#name.discard("Rachel")
name.discard("Doe")
print(name)
print("--------------------------------------------------")


#intersection
num1={1,2,3,4,5}
num2={4,5,8}
result=num1.intersection(num2)
print(result)
print("--------------------------------------------------")


#is Subset
a={1,5}
b={7,5,3}
print(a.issubset(b))
print("--------------------------------------------------")


#is Superset
a={1,5}
b={7,5,3}
print(a.issuperset(b))
print("--------------------------------------------------")


#pop
w = {"q", 5, "e", "r"}
w = w.pop()
print(w)
print("--------------------------------------------------")


#remove
num = { 3,5,7}
num.remove(5)
print(num)
print("--------------------------------------------------")


#symmetric difference
num1={1,2,3,4,5}
num2={4,5,8}
result=num1.symmetric_difference(num2)    
print(result)
print("--------------------------------------------------")

#union
Alpha = {"a", "b", "c"}
Beta = {"d", "e", "f"}
Gamma = Alpha.union(Beta)
print(Gamma)
print("--------------------------------------------------")

#update
num1 = {1,3}
num1.update([1,55,6])
print(num1)