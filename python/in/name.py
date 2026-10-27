t = {"name": "john", "age": 25}
t = {"name": "john", "age": 25, "city": "new york", "Nation": "USA"}

# print(t["age"])


# t.update({"age": 26, "address": "123 boston"})
# print(t)


print(t.keys())
print(t.values())
print(t.items() )


#remove
# print(t.pop("Nation"))
print(t.popitem())
print(t)


#if it is same value it will replace by the new value, if not it will add
t.setdefault("gender", "male")
print(t)


#clear all value
print(t.clear())
print(t)
