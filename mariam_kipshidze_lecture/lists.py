"""List Methods"""
# Initial list
fruits = ['apple', 'banana', 'cherry']

# 1. append() - Add an element to the end of the list
fruits.append('pear')
print("After append:", fruits)

# 2. extend() - Add all elements of a list to the end of the current list
fruits.extend(['grape', 'watermelon'])
print("After extend:", fruits)

# 3. insert() - Insert an element at a specific position
fruits.insert(2, 'blueberry')
print("After insert:", fruits)

# 4. remove() - Remove the first occurrence of a specific element
fruits.remove('cherry')
print("After remove:", fruits)

# 5. pop() - Remove and return the element at a specific position (or last if no index is provided)
popped_fruit = fruits.pop()
print("After pop (no index):", fruits, "Popped:", popped_fruit)

popped_fruit_at_index = fruits.pop(2)
print("After pop (index 2):", fruits, "Popped:", popped_fruit_at_index)

# 6. clear() - Remove all elements from the list
fruits.clear()
print("After clear:", fruits)

# Re-initialize list
fruits = ['apple', 'banana', 'cherry']

# 7. index() - Return the index of the first occurrence of a specific element
index_of_cherry = fruits.index('cherry')
print("Index of 'cherry':", index_of_cherry)

# 8. count() - Return the number of occurrences of a specific element
count_of_apple = fruits.count('apple')
print("Count of 'apple':", count_of_apple)

# 9. sort() - Sort the list in ascending order (can be customized with key and reverse)
fruits.sort()
print("After sort:", fruits)

# 10. reverse() - Reverse the order of the list
fruits.reverse()
print("After reverse:", fruits)

# 11. copy() - Return a shallow copy of the list
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)

# 12. len() - Return the number of items in the list
length_of_fruits = len(fruits)
print("Length of the list:", length_of_fruits)
