import random

# Example 1: Generate a random floating-point number between 0.0 and 1.0
random_number = random.random()
print("Random number between 0.0 and 1.0:", random_number)

# Example 2: Generate a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print("Random integer between 1 and 10:", random_integer)

# Example 3: Choose a random item from a list
items = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(items)
print("Random item:", random_item)
