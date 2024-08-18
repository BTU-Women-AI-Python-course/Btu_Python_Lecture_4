# clear
dict1 = {"key1": "value1", "key2": "value2"}

dict1.clear()
print(dict1)

# copy
dict1 = {"key1": "value1", "key2": "value2"}
dict2 = dict1.copy()
dict2["key3"] = "value3"
print(dict1)
print(dict2)

# from keys
x = ['key1', 'key2', 'key3']

thisdict = dict.fromkeys(x, 0)

print(thisdict)

# get
dict1 = {"key1": "value1", "key2": "value2"}

print(dict1.get('key5', "Not Found"))

# items
dict1 = {"key1": "value1", "key2": "value2"}

for key, value in dict1.items():
    print(key, value)


# keys
dict1 = {"key1": "value1", "key2": "value2"}

keys = dict1.keys()
print(keys)

# pop
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.pop("model")

print(car)

# pop item
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.popitem()
print(car)

# set default
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model1", "Bronco")

print(x)

# update
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "color": "blue"
}

car.update({"color": "White"})

print(car)

# values
dict1 = {"key1": "value1", "key2": "value2"}

print(dict1.keys())