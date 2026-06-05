# Python Built-in Functions Tutorial
# This file covers Python's built-in functions and how map, filter, sum,
# max, min, any, all, and lambda expressions help write concise code.

# ============================================================
# 1. LAMBDA FUNCTIONS
# ============================================================
# A lambda is a small anonymous function created with the lambda keyword.
# It is useful when you need a quick function without defining a named one.

print("--- Lambda Functions ---")

# Regular function


def add(a, b):
    return a + b


print("add(2, 3):", add(2, 3))

# Lambda function equivalent
add_lambda = lambda a, b: a + b
print("add_lambda(2, 3):", add_lambda(2, 3))

# Lambdas are often used when a simple function is needed quickly
square = lambda x: x * x
print("square(5):", square(5))

# Lambdas can be passed directly into built-in functions
print("lambda in sorted:", sorted([3, 1, 2], key=lambda x: -x))

# ============================================================
# 2. MAP
# ============================================================
# map() applies a function to each item in an iterable and returns an iterator.
# It is useful for transforming data without writing an explicit loop.

print("\n--- map() ---")

numbers = [1, 2, 3, 4, 5]

# Use map with a named function
print("Doubled with map:", list(map(lambda x: x * 2, numbers)))

# Use map with a lambda to convert to strings
strings = list(map(lambda x: f"Number {x}", numbers))
print("Strings from numbers:", strings)

# Map can accept multiple iterables if the function expects multiple arguments
numbers2 = [10, 20, 30, 40, 50]
sum_pairs = list(map(lambda a, b: a + b, numbers, numbers2))
print("Sum pairs:", sum_pairs)

# ============================================================
# 3. FILTER
# ============================================================
# filter() keeps items from an iterable when a function returns True.
# It is useful for selecting values based on a condition.

print("\n--- filter() ---")

# Keep even numbers from the list
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Keep strings that start with a certain letter
tokens = ["apple", "banana", "avocado", "berry"]
a_words = list(filter(lambda s: s.startswith("a"), tokens))
print("Words starting with 'a':", a_words)

# filter returns an iterator, so convert to list or iterate directly
print("Filter output as list:", list(filter(lambda x: x > 3, numbers)))

# ============================================================
# 4. SUM
# ============================================================
# sum() adds numeric values from an iterable.
# It is reliable, readable, and handles large iterables lazily when used with generators.

print("\n--- sum() ---")

print("Sum of numbers:", sum(numbers))
print("Sum of squares:", sum(x * x for x in numbers))
print("Sum with start value:", sum(numbers, 10))  # starts at 10

# ============================================================
# 5. MAX and MIN
# ============================================================
# max() and min() find the largest and smallest items in an iterable.
# They can take an optional key function for custom comparisons.

print("\n--- max() and min() ---")

values = [8, 3, 10, 1, 6]
print("Max value:", max(values))
print("Min value:", min(values))

# Use a key function to compare by absolute value
mixed = [-7, 2, -10, 3]
print("Max by absolute value:", max(mixed, key=abs))
print("Min by absolute value:", min(mixed, key=abs))

# Find the longest word in a list
words = ["apple", "banana", "kiwi", "strawberry"]
print("Longest word:", max(words, key=len))
print("Shortest word:", min(words, key=len))

# ============================================================
# 6. ANY and ALL
# ============================================================
# any() returns True if at least one item is truthy.
# all() returns True only if all items are truthy.
# They are useful for readability in boolean checks.

print("\n--- any() and all() ---")

values = [0, None, False, "text"]
print("any(values):", any(values))
print("all(values):", all(values))

numbers = [2, 4, 6, 8]
print("All even?", all(x % 2 == 0 for x in numbers))
print("Any even?", any(x % 2 == 0 for x in [1, 3, 5, 8]))

# any() and all() are short-circuiting: they stop as soon as the result is known

# ============================================================
# 7. WHY USE BUILT-INS?
# ============================================================
# Built-in functions are optimized and often faster than equivalent Python loops.
# They help keep code concise and expressive.

print("\n--- Built-in Function Advantages ---")

print("map/filter are concise for data transformation and selection.")
print("sum/max/min are easy to read and designed for numeric aggregates.")
print("any/all simplify boolean checks over iterables.")
print("lambda helps build small inline functions without extra definitions.")

# Practical example: process a list of temperatures

temps = [72, 65, 88, 91, 55, 78]

# Convert temperatures to strings with map
print("Temperature strings:", list(map(lambda t: f"{t}F", temps)))

# Filter temperatures above 80
hot_days = list(filter(lambda t: t > 80, temps))
print("Hot days:", hot_days)

# Compute statistics using built-ins
print("Average temp:", sum(temps) / len(temps))
print("Highest temp:", max(temps))
print("Lowest temp:", min(temps))
print("Any hot days?", any(t > 80 for t in temps))
print("All days above freezing?", all(t > 32 for t in temps))

# ============================================================
# 8. ZIP, ENUMERATE, REVERSED, SORTED
# ============================================================
print("\n--- zip(), enumerate(), reversed(), sorted() ---")

letters = ["a", "b", "c"]
numbers = [1, 2, 3]
more_numbers = [10, 20]

# zip pairs items from multiple iterables, stopping at the shortest one.
print("zip letters and numbers:", list(zip(letters, numbers)))
print("zip with unequal lengths:", list(zip(letters, more_numbers)))

# You can also unpack zipped pairs directly into variables.
paired = list(zip(letters, numbers))
for letter, number in paired:
    print(f"{letter} -> {number}")

# enumerate gives an index and the value for each item.
print("enumerate letters:", list(enumerate(letters)))
for index, letter in enumerate(letters, start=1):
    print(f"Letter {index}: {letter}")

# reversed returns an iterator that walks a sequence backwards.
print("reversed numbers:", list(reversed(numbers)))
print("reverse a string with reversed:", "".join(reversed("abc")))

# sorted returns a new list and leaves the original unchanged.
unsorted_values = [5, 2, 9, 1]
print("sorted values:", sorted(unsorted_values))
print("original unchanged:", unsorted_values)

# Use key to sort by custom criteria, and reverse to invert order.
print("sorted by absolute value:", sorted([-3, 1, -2], key=abs))
people = [("Anna", 28), ("Bob", 22), ("Carol", 35)]
print("sorted by age:", sorted(people, key=lambda item: item[1]))
print(
    "sorted by name descending:", sorted(people, key=lambda item: item[0], reverse=True)
)

# ============================================================
# 9. ID, HASH, DIR, GLOBALS, LOCALS
# ============================================================
print("\n--- id(), hash(), dir(), globals(), locals() ---")

value = "hello"
print("id(value):", id(value))
print("hash(value):", hash(value))

# id() gives a stable identity for the object while it exists.
# hash() returns a value used by dictionaries and sets for fast lookup.
print("hash of a tuple:", hash((1, 2, 3)))
try:
    print("hash of a list:", hash([1, 2, 3]))
except TypeError as exc:
    print("list is unhashable:", exc)

# dir() lists attributes and methods for an object or module.
print("dir(value) sample:", [name for name in dir(value) if name.startswith("is")][:5])
print(
    "dir(people) sample:", [name for name in dir(people) if name.startswith("co")][:5]
)

# globals() returns the module-level namespace dictionary.
print("'numbers' in globals():", "numbers" in globals())


# locals() returns the current local namespace dictionary.
def show_locals():
    local_var = 123
    print("local_var in locals():", "local_var" in locals())
    print("locals() keys sample:", list(locals().keys())[:5])


show_locals()

# In a function, modifying locals() may not update actual local variables.
# Use locals() mainly for inspection.

# ============================================================
# 10. TYPE CHECKS AND ATTRIBUTE ACCESS
# ============================================================
print(
    "\n--- isinstance(), issubclass(), getattr(), setattr(), hasattr(), delattr() ---"
)


class Animal:
    pass


class Dog(Animal):
    def __init__(self, name):
        self.name = name


print("isinstance(Dog('Fido'), Dog):", isinstance(Dog("Fido"), Dog))
print("isinstance(Dog('Fido'), Animal):", isinstance(Dog("Fido"), Animal))
print("isinstance(Dog('Fido'), object):", isinstance(Dog("Fido"), object))
print("issubclass(Dog, Animal):", issubclass(Dog, Animal))
print("issubclass(Animal, Dog):", issubclass(Animal, Dog))

pet = Dog("Fido")
print("hasattr(pet, 'name'):", hasattr(pet, "name"))
print("getattr(pet, 'name'):", getattr(pet, "name"))
print("getattr(pet, 'age', 'unknown'):", getattr(pet, "age", "unknown"))
setattr(pet, "age", 5)
print("getattr(pet, 'age') after setattr:", getattr(pet, "age"))
delattr(pet, "age")
print("hasattr(pet, 'age') after delattr:", hasattr(pet, "age"))

# getattr() with a default avoids AttributeError when the attribute is missing.

# ============================================================
# 11. ITER and NEXT
# ============================================================
print("\n--- iter() and next() ---")

iterable = [10, 20, 30]
iterator = iter(iterable)
print("next(iterator):", next(iterator))
print("next(iterator):", next(iterator))
print("next(iterator):", next(iterator))

# Manual iteration with next() must handle StopIteration.
iterator = iter(iterable)
while True:
    try:
        item = next(iterator)
        print("got:", item)
    except StopIteration:
        print("iterator exhausted")
        break

# iter() can also create a sentinel iterator from a callable.
with open(__file__, "r") as f:
    line_iter = iter(f.readline, "")
    print("first line from file using sentinel iter():", next(line_iter).strip())

# Iterators are single-pass objects. Once exhausted, they do not restart.

# ============================================================
# 12. CALLABLE
# ============================================================
print("\n--- callable() ---")

print("callable(add):", callable(add))
print("callable(42):", callable(42))
print("callable(lambda x: x):", callable(lambda x: x))
print("callable(Dog):", callable(Dog))


class Greeter:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"


say_hello = Greeter("Hello")
print("callable(say_hello):", callable(say_hello))
print("say_hello('World'):", say_hello("World"))

# callable() is useful when you accept either a function or an object that behaves like one.

# ============================================================
# 13. EVAL and EXEC
# ============================================================
print("\n--- eval() and exec() ---")

expr = "2 + 3 * 4"
print("eval(expr):", eval(expr))

# eval() can use a specific globals dictionary for controlled evaluation.
namespace = {"x": 5}
print("eval('x + 1', namespace):", eval("x + 1", namespace))

# exec() runs statements and can define new names in a namespace.
code = 'result = 10\nprint("exec result:", result)'
exec(code, namespace)
print("namespace['result']:", namespace.get("result"))

# Use eval and exec carefully; they execute dynamic code and can be unsafe with untrusted input.
# For simple literal parsing, prefer ast.literal_eval instead of eval.
import ast

safe_value = ast.literal_eval("[1, 2, 3]")
print("ast.literal_eval safe parse:", safe_value)

# ============================================================
# 14. SUMMARY
# ============================================================
print("\n=== Summary ===")
print("- lambda creates small anonymous functions for quick use.")
print("- map() transforms iterable values with a function.")
print("- filter() selects iterable values that match a condition.")
print("- sum() adds numeric values from an iterable.")
print("- max() and min() find the largest and smallest values.")
print("- any() returns True if any item is truthy.")
print("- all() returns True only if every item is truthy.")
print("- zip() pairs items from multiple iterables.")
print("- enumerate() adds index numbers to iterable items.")
print("- reversed() iterates over items in reverse order.")
print("- sorted() returns a new sorted list and preserves the original.")
print("- id() returns an object's identity, hash() returns its hash value.")
print("- dir() lists an object's attributes and methods.")
print("- globals() and locals() expose current namespace dictionaries.")
print("- isinstance() and issubclass() validate object types and inheritance.")
print("- getattr()/setattr()/hasattr()/delattr() inspect and modify object attributes.")
print("- iter() and next() let you manually walk through iterators.")
print("- callable() checks whether an object can be invoked like a function.")
print("- eval() evaluates expressions dynamically, and exec() runs dynamic code.")
print("- Built-ins are concise, expressive, and often faster than manual loops.")
