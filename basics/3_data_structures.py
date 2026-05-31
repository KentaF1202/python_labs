# Python Data Structures Tutorial
# This file covers the main data structures in Python: lists, tuples, dictionaries, and sets

# ============================================================
# 1. LISTS
# ============================================================
# A list is an ordered, mutable (changeable) collection of items
# Items are stored in a specific order and can be modified
# Lists are created with square brackets []

print("=" * 60)
print("1. LISTS")
print("=" * 60)

# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]  # Lists can contain different types
empty_list = []

print(f"Fruits list: {fruits}")
print(f"Numbers list: {numbers}")
print(f"Mixed types list: {mixed}")

# Accessing list items using indices (0-based indexing)
print(f"\nFirst fruit: {fruits[0]}")  # Index 0
print(f"Second fruit: {fruits[1]}")  # Index 1
print(f"Last fruit: {fruits[-1]}")  # Index -1 (last item)
print(f"Second to last: {fruits[-2]}")  # Index -2

# List slicing - getting a portion of a list
print(f"\nFirst two fruits: {fruits[0:2]}")  # From index 0 to 1
print(f"From index 1 onwards: {fruits[1:]}")  # From index 1 to end
print(f"All but the last: {fruits[:-1]}")  # All except last
print(f"Every second item: {numbers[::2]}")  # Start:Stop:Step

# Modifying lists
print(f"\nOriginal fruits: {fruits}")
fruits[0] = "grape"  # Change first item
print(f"After changing first item: {fruits}")

# Adding items to a list
fruits.append("mango")  # Add one item to the end
print(f"After append: {fruits}")

fruits.insert(1, "kiwi")  # Insert at specific position
print(f"After insert at position 1: {fruits}")

fruits.extend(["pear", "peach"])  # Add multiple items
print(f"After extend: {fruits}")

# Removing items from a list
fruits.remove("kiwi")  # Remove by value
print(f"After removing 'kiwi': {fruits}")

last_fruit = fruits.pop()  # Remove and return last item
print(f"After pop: {fruits}, removed: {last_fruit}")

# Useful list methods
print(f"\nLength of fruits: {len(fruits)}")
print(f"Index of 'banana': {fruits.index('banana')}")
print(f"Is 'apple' in fruits? {'apple' in fruits}")
print(f"Sorted fruits: {sorted(fruits)}")

# Sorting (modifies the original list)
numbers_unsorted = [5, 2, 8, 1, 9]
numbers_unsorted.sort()
print(f"Sorted numbers: {numbers_unsorted}")

# Reversing
numbers_unsorted.reverse()
print(f"Reversed: {numbers_unsorted}")

# ============================================================
# 2. TUPLES
# ============================================================
# A tuple is an ordered, immutable (unchangeable) collection
# Once created, you cannot modify a tuple
# Tuples are created with parentheses ()

print("\n" + "=" * 60)
print("2. TUPLES")
print("=" * 60)

# Creating tuples
colors = ("red", "green", "blue")
single_item = (42,)  # Note: needs a comma for single-item tuple
empty_tuple = ()
numbers_tuple = (1, 2, 3, 4, 5)

print(f"Colors tuple: {colors}")
print(f"Single item tuple: {single_item}")
print(f"Numbers tuple: {numbers_tuple}")

# Accessing items (same as lists)
print(f"\nFirst color: {colors[0]}")
print(f"Last color: {colors[-1]}")
print(f"Slice [0:2]: {colors[0:2]}")

# You cannot modify tuples (this would cause an error if uncommented)
# colors[0] = "yellow"  # TypeError!

# Tuple unpacking - extract values into separate variables
print(f"\nTuple unpacking:")
color1, color2, color3 = colors
print(f"color1: {color1}, color2: {color2}, color3: {color3}")

# Tuples are useful for returning multiple values from functions
def get_coordinates():
    return (10, 20)  # Return multiple values as a tuple

x, y = get_coordinates()
print(f"Coordinates: x={x}, y={y}")

# Tuple methods
print(f"\nLength of colors: {len(colors)}")
print(f"Count of 'red' in colors: {colors.count('red')}")
print(f"Index of 'green': {colors.index('green')}")

# Converting between lists and tuples
list_from_tuple = list(colors)
tuple_from_list = tuple([1, 2, 3])
print(f"List from tuple: {list_from_tuple}")
print(f"Tuple from list: {tuple_from_list}")

# ============================================================
# 3. DICTIONARIES
# ============================================================
# A dictionary is an unordered, mutable collection of key-value pairs
# Each item has a key and a value
# Dictionaries are created with curly braces {}

print("\n" + "=" * 60)
print("3. DICTIONARIES")
print("=" * 60)

# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}

scores = {"math": 95, "english": 87, "science": 92}
empty_dict = {}

print(f"Person dictionary: {person}")
print(f"Scores: {scores}")

# Accessing values using keys
print(f"\nPerson's name: {person['name']}")
print(f"Math score: {scores['math']}")

# Safe access with .get() (returns None if key doesn't exist)
print(f"Age: {person.get('age')}")
print(f"Country: {person.get('country')}")  # Returns None
print(f"Country with default: {person.get('country', 'Unknown')}")

# Modifying dictionaries
print(f"\nOriginal person: {person}")
person['age'] = 31  # Change a value
print(f"After changing age: {person}")

person['country'] = "USA"  # Add a new key-value pair
print(f"After adding country: {person}")

# Removing items
del person['country']  # Delete a key-value pair
print(f"After deleting country: {person}")

removed_value = person.pop('job')  # Remove and return value
print(f"After pop (removed '{removed_value}'): {person}")

# Useful dictionary methods
print(f"\nKeys in person: {list(person.keys())}")
print(f"Values in person: {list(person.values())}")
print(f"Items in person: {list(person.items())}")

print(f"\nIs 'name' in person? {'name' in person}")
print(f"Length of person: {len(person)}")

# Iterating through dictionaries
print(f"\nIterating through person:")
for key in person:
    print(f"  {key}: {person[key]}")

print(f"\nIterating with .items():")
for key, value in person.items():
    print(f"  {key}: {value}")

# Updating dictionaries
person.update({"age": 32, "hobby": "coding"})
print(f"After update: {person}")

# ============================================================
# 4. SETS
# ============================================================
# A set is an unordered, mutable collection of unique items
# Duplicates are automatically removed
# Sets are created with curly braces {} (but must have items to distinguish from dict)

print("\n" + "=" * 60)
print("4. SETS")
print("=" * 60)

# Creating sets
fruits_set = {"apple", "banana", "orange", "banana"}  # Duplicates removed
numbers_set = {1, 2, 3, 4, 5}
empty_set = set()  # Must use set() for empty set

print(f"Fruits set: {fruits_set}")  # Note: only one 'banana'
print(f"Numbers set: {numbers_set}")
print(f"Empty set: {empty_set}")

# Adding items
fruits_set.add("mango")
print(f"After adding 'mango': {fruits_set}")

fruits_set.add("apple")  # Adding duplicate does nothing
print(f"After adding 'apple' (duplicate): {fruits_set}")

# Removing items
fruits_set.remove("banana")  # Raises error if item not found
print(f"After removing 'banana': {fruits_set}")

fruits_set.discard("grape")  # No error if item not found
print(f"After discarding 'grape' (not in set): {fruits_set}")

# Set operations (useful for comparing collections)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"\nSet A: {set_a}")
print(f"Set B: {set_b}")

# Union - all items from both sets
print(f"Union (A | B): {set_a | set_b}")
print(f"Union using .union(): {set_a.union(set_b)}")

# Intersection - items in both sets
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Intersection using .intersection(): {set_a.intersection(set_b)}")

# Difference - items in A but not in B
print(f"Difference (A - B): {set_a - set_b}")
print(f"Difference using .difference(): {set_a.difference(set_b)}")

# Symmetric difference - items in either A or B but not both
print(f"Symmetric difference (A ^ B): {set_a ^ set_b}")

# Checking membership
print(f"\n3 in set_a? {3 in set_a}")
print(f"5 in set_a? {5 in set_a}")

# Useful set methods
print(f"Length of set_a: {len(set_a)}")
print(f"Is set_a a subset of (1,2,3,4,5)? {set_a <= {1, 2, 3, 4, 5}}")
print(f"Is set_a a superset of (1,2)? {set_a >= {1, 2}}")

# ============================================================
# 5. LIST COMPREHENSIONS
# ============================================================
# A concise way to create lists based on existing lists
# Syntax: [expression for item in iterable if condition]

print("\n" + "=" * 60)
print("5. LIST COMPREHENSIONS")
print("=" * 60)

# Basic list comprehension - square each number
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Original: {numbers}")
print(f"Squares: {squares}")

# List comprehension with a condition - only even numbers
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# List comprehension with transformation and condition
words = ["apple", "banana", "cherry", "date"]
long_words = [word.upper() for word in words if len(word) > 4]
print(f"Long words (uppercase): {long_words}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Flattened matrix: {flattened}")

# List comprehension with string manipulation
letters = ["a", "b", "c"]
repeated = [letter * 3 for letter in letters]
print(f"Repeated letters: {repeated}")

# Equivalent without list comprehension (for comparison)
print(f"\nWithout list comprehension:")
squares_old = []
for x in numbers:
    squares_old.append(x**2)
print(f"Squares (old way): {squares_old}")

# ============================================================
# 6. DICTIONARY COMPREHENSIONS
# ============================================================
# Similar to list comprehensions but for dictionaries
# Syntax: {key_expr: value_expr for item in iterable if condition}

print("\n" + "=" * 60)
print("6. DICTIONARY COMPREHENSIONS")
print("=" * 60)

# Basic dictionary comprehension - create number: square pairs
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(f"Number to square mapping: {squares_dict}")

# Dictionary comprehension with condition
even_squares = {x: x**2 for x in numbers if x % 2 == 0}
print(f"Even numbers and their squares: {even_squares}")

# Create dictionary from lists
keys = ["name", "age", "city"]
values = ["Bob", 25, "London"]
person_dict = {k: v for k, v in zip(keys, values)}
print(f"Created dict from keys and values: {person_dict}")

# Transform existing dictionary
prices = {"apple": 1.0, "banana": 0.5, "orange": 0.75}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(f"Original prices: {prices}")
print(f"With 10% discount: {discounted}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped keys/values: {swapped}")

# ============================================================
# 7. SET COMPREHENSIONS
# ============================================================
# Similar to list comprehensions but for sets

print("\n" + "=" * 60)
print("7. SET COMPREHENSIONS")
print("=" * 60)

# Basic set comprehension
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x**2 for x in numbers}
print(f"Original (with duplicates): {numbers}")
print(f"Unique squares: {unique_squares}")

# Set comprehension with condition
even_squares_set = {x**2 for x in range(10) if x % 2 == 0}
print(f"Squares of even numbers 0-9: {even_squares_set}")

# ============================================================
# 8. PRACTICAL EXAMPLES
# ============================================================
print("\n" + "=" * 60)
print("8. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Processing student data
students = {
    "Alice": [85, 90, 88],
    "Bob": [92, 88, 95],
    "Charlie": [78, 85, 80]
}

# Calculate average for each student using dict comprehension
averages = {name: sum(scores) / len(scores) for name, scores in students.items()}
print(f"Student averages: {averages}")

# Example 2: Find students with average above 85
top_students = {name: avg for name, avg in averages.items() if avg >= 85}
print(f"Top students (avg >= 85): {top_students}")

# Example 3: Count word frequencies
text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
word_count = {word: words.count(word) for word in set(words)}
print(f"Word frequencies: {word_count}")

# Example 4: Remove duplicates while preserving order
items = [1, 2, 2, 3, 1, 4, 3, 5]
unique_items = list(dict.fromkeys(items))  # Preserves order (Python 3.7+)
print(f"Items with duplicates: {items}")
print(f"Unique items (ordered): {unique_items}")

# Example 5: Group numbers into categories
numbers = [10, 23, 45, 12, 67, 34, 89, 5]
categories = {
    "small": [x for x in numbers if x < 20],
    "medium": [x for x in numbers if 20 <= x < 60],
    "large": [x for x in numbers if x >= 60]
}
print(f"Numbers by category: {categories}")

# ============================================================
# 9. SUMMARY AND KEY POINTS
# ============================================================
print("\n" + "=" * 60)
print("9. SUMMARY AND KEY POINTS")
print("=" * 60)

summary = """
LISTS:
  - Ordered, mutable, allows duplicates
  - Use when you need to maintain order and modify items
  - Syntax: [1, 2, 3]

TUPLES:
  - Ordered, immutable, allows duplicates
  - Use when you need to protect data from modification
  - Syntax: (1, 2, 3)

DICTIONARIES:
  - Unordered, mutable, key-value pairs
  - Use to store related data with meaningful keys
  - Syntax: {"key": "value"}

SETS:
  - Unordered, mutable, no duplicates
  - Use for membership testing and removing duplicates
  - Syntax: {1, 2, 3}

COMPREHENSIONS:
  - Concise way to create lists, dicts, and sets
  - More readable than loops
  - Can include conditions for filtering
"""

print(summary)
print("=" * 60)
print("End of Data Structures Tutorial")
print("=" * 60)
