# Example 1: Sort a list of numbers in ascending order
numbers = [5, 3, 9, 1, 7]
numbers.sort()
print("Sorted numbers (ascending):", numbers)

"============================================================"

# Example 2: Sort a list of numbers in descending order
numbers = [5, 3, 9, 1, 7]
numbers.sort(reverse=True)
print("Sorted numbers (descending):", numbers)

"============================================================"

# Example 3: Sort a list of strings alphabetically
words = ["banana", "apple", "cherry", "date"]
words.sort()
print("Sorted words (alphabetically):", words)

"============================================================"

# Example 4: Sort a list of strings by length
words = ["banana", "apple", "cherry", "date"]
words.sort(key=len)
print("Sorted words (by length):", words)

"============================================================"

# Example 5: Sort a list of tuples by the second element
tuples = [(1, 3), (2, 1), (3, 2)]
tuples.sort(key=lambda x: x[1])
print("Sorted tuples (by second element):", tuples)

"============================================================"

# Example 6: Sort a list of dictionaries by a specific key
dicts = [{'name': 'John', 'age': 45}, {'name': 'Jane', 'age': 29}, {'name': 'Doe', 'age': 34}]
dicts.sort(key=lambda x: x['age'])
print("Sorted dictionaries (by age):", dicts)
