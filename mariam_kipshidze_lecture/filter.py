# Example 1: Filter even numbers from a list
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

"============================================================"

# Example 2: Filter words that are longer than 4 letters
def is_long_word(word):
    return len(word) > 4

words = ["apple", "cat", "dog", "banana", "kiwi"]
long_words = list(filter(is_long_word, words))
print("Words longer than 4 letters:", long_words)

"============================================================"

# Example 3: Filter negative numbers from a list
def is_non_negative(x):
    return x >= 0

mixed_numbers = [-5, 3, -1, 101, -50, 32, 0, -12]
positive_numbers = list(filter(is_non_negative, mixed_numbers))
print("Non-negative numbers:", positive_numbers)

"============================================================"

# Example 4: Filter out None values from a list
def is_not_none(x):
    return x is not None

values = [None, "Hello", "", 0, None, 5, "World"]
non_none_values = list(filter(is_not_none, values))
print("Values without None:", non_none_values)

"============================================================"

# Example 5: Filter out empty strings from a list
def is_not_empty(s):
    return s.strip() != ""

strings = ["apple", "", "banana", " ", "cherry", ""]
non_empty_strings = list(filter(is_not_empty, strings))
print("Non-empty strings:", non_empty_strings)

"============================================================"

# Example 6: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

"============================================================"

# Example 7: Filter words that are longer than 4 letters
words = ["apple", "cat", "dog", "banana", "kiwi"]
long_words = list(filter(lambda word: len(word) > 4, words))
print("Words longer than 4 letters:", long_words)
