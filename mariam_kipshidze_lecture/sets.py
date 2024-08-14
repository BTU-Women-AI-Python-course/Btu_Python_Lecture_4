"""Set Methods"""
# Initial set
fruits = {'apple', 'banana', 'cherry'}

# 1. add() - Add an element to the set
fruits.add('elderberry')
print("After add:", fruits)

# 2. update() - Add multiple elements to the set
fruits.update(['grape', 'watermelon'])
print("After update:", fruits)

# 3. remove() - Remove an element from the set (raises KeyError if the element is not found)
fruits.remove('banana')
print("After remove:", fruits)

# 4. discard() - Remove an element from the set (does not raise an error if the element is not found)
fruits.discard('cherry')
print("After discard:", fruits)

# 5. pop() - Remove and return an arbitrary element from the set
popped_fruit = fruits.pop()
print("After pop:", fruits, "Popped:", popped_fruit)

# 6. clear() - Remove all elements from the set
fruits.clear()
print("After clear:", fruits)

# Re-initialize set
fruits = {'apple', 'banana', 'cherry', 'date'}

# 7. union() - Return a new set with elements from the set and all others
more_fruits = {'elderberry', 'fig'}
all_fruits = fruits.union(more_fruits)
print("Union:", all_fruits)

# 8. intersection() - Return a new set with elements common to the set and others
common_fruits = fruits.intersection({'banana', 'fig', 'apple'})
print("Intersection:", common_fruits)

# 9. difference() - Return a new set with elements in the set that are not in the others
different_fruits = fruits.difference({'banana', 'date'})
print("Difference:", different_fruits)

# 10. symmetric_difference() - Return a new set with elements in either the set or the others but not both
symmetric_diff_fruits = fruits.symmetric_difference({'banana', 'date', 'elderberry'})
print("Symmetric Difference:", symmetric_diff_fruits)

# 11. issubset() - Check if the set is a subset of another
is_subset = {'apple', 'banana'}.issubset(fruits)
print("Is subset:", is_subset)

# 12. issuperset() - Check if the set is a superset of another
is_superset = fruits.issuperset({'apple', 'banana'})
print("Is superset:", is_superset)

# 13. isdisjoint() - Check if two sets have no elements in common
is_disjoint = fruits.isdisjoint({'fig', 'grape'})
print("Is disjoint:", is_disjoint)

# 14. len() - Return the number of elements in the set
length_of_fruits = len(fruits)
print("Length of the set:", length_of_fruits)

# 15. Checking membership
is_apple_in_fruits = 'apple' in fruits
print("Is 'apple' in fruits:", is_apple_in_fruits)

# 16. Iterating through a set
print("Iterating through set:")
for fruit in fruits:
    print(fruit)

# 17. Copying a set
fruits_copy = fruits.copy()
print("Copied set:", fruits_copy)

print(id(fruits_copy))
print(id(fruits))
