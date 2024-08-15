# Dictionary Methods with Examples

# Creating a sample dictionary
sample_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Developer"
}

# 1. clear()
# Removes all items from the dictionary
sample_dict.clear()
print("After clear:", sample_dict)

# 2. copy()
# Returns a shallow copy of the dictionary
sample_dict = {"name": "Alice", "age": 25}
copy_dict = sample_dict.copy()
print("Copy:", copy_dict)

# 3. fromkeys()
# Creates a new dictionary from a sequence of keys and a value
keys = ["name", "age", "city"]
default_value = None
new_dict = dict.fromkeys(keys, default_value)
print("From keys:", new_dict)

# 4. get()
# Returns the value for a specified key if the key is in the dictionary
age = sample_dict.get("age")
print("Get age:", age)

# 5. items()
# Returns a view object that displays a list of a
# dictionary's key-value tuple pairs
items = sample_dict.items()
print("Items:", list(items))

# 6. keys()
# Returns a view object that displays a list of all the keys in the dictionary
keys = sample_dict.keys()
print("Keys:", list(keys))

# 7. pop()
# Removes the specified key and returns the corresponding value
age = sample_dict.pop("age")
print("Popped age:", age)
print("After pop:", sample_dict)

# 8. popitem()
# Removes and returns the last inserted key-value pair
sample_dict["age"] = 25
last_item = sample_dict.popitem()
print("Popped item:", last_item)
print("After popitem:", sample_dict)

# 9. setdefault()
# Returns the value of a specified key.
# If the key does not exist, insert the key with a specified value.
city = sample_dict.setdefault("city", "Unknown")
print("Set default city:", city)
print("After setdefault:", sample_dict)

# 10. update()
# Updates the dictionary with the specified key-value pairs
sample_dict.update({"age": 25, "job": "Developer"})
print("After update:", sample_dict)

# 11. values()
# Returns a view object that displays a list of all the values in the dictionary
values = sample_dict.values()
print("Values:", list(values))
