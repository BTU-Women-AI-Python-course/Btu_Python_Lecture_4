"""Tuple Methods"""
# Initial tuple
fruits = ('apple', 'banana', 'cherry')

# 1. count() - Return the number of occurrences of a specific element
count_of_apple = fruits.count('apple')
print("Count of 'apple':", count_of_apple)

# 2. index() - Return the index of the first occurrence of a specific element
index_of_cherry = fruits.index('cherry')
print("Index of 'cherry':", index_of_cherry)

# Additional tuple operations (since tuples are immutable)

# 3. Accessing elements (indexing)
first_fruit = fruits[0]
print("First fruit:", first_fruit)

# 4. Slicing
slice_of_fruits = fruits[1:2]
print("Slice of fruits (1:2):", slice_of_fruits)

# 5. Concatenation - Combine two tuples
more_fruits = ('grape', 'watermelon')
all_fruits = fruits + more_fruits
print("After concatenation:", all_fruits)

# 6. Repeating - Repeat the tuple elements
repeated_fruits = fruits * 2
print("After repeating:", repeated_fruits)

# 7. Length - Return the number of items in the tuple
length_of_fruits = len(fruits)
print("Length of the tuple:", length_of_fruits)

# 8. Checking membership
is_banana_in_fruits = 'banana' in fruits
print("Is 'banana' in fruits:", is_banana_in_fruits)

# 9. Iterating through a tuple
print("Iterating through tuple:")
for fruit in fruits:
    print(fruit)

# 10. Tuple unpacking
a, b, c = fruits
print("Unpacked tuple:", a, b, c)
