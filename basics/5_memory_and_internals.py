# Python Memory and Internals Basics
# This file covers mutable vs immutable types, identity vs equality,
# variable scope, and garbage collection.

# ============================================================
# 1. MUTABLE VS IMMUTABLE
# ============================================================
# Mutable objects can be changed after creation.
# Immutable objects cannot be changed after creation.

print("--- Mutable vs Immutable ---")

# Examples of immutable types:
number = 10
text = "hello"
tuple_data = (1, 2, 3)

print("Number before:", number)
number = 20  # This makes number refer to a new integer object
print("Number after:", number)

# Strings are immutable, so operations create a new string
print("Text before:", text)
new_text = text.upper()
print("Text after upper():", new_text)
print("Original text still:", text)

# Lists are mutable: their contents can change in place
my_list = [1, 2, 3]
print("List before:", my_list)
my_list.append(4)
print("List after append:", my_list)
my_list[0] = 10
print("List after assignment:", my_list)

# Dictionaries are also mutable
my_dict = {"a": 1, "b": 2}
print("Dict before:", my_dict)
my_dict["c"] = 3
print("Dict after adding key c:", my_dict)

# ============================================================
# 2. IDENTITY vs EQUALITY
# ============================================================
# '==' checks equality of values.
# 'is' checks whether two names point to the same object in memory.

print("\n--- Identity vs Equality ---")

# For immutable values, Python may reuse objects internally
x = 1000
y = 1000
print("x == y:", x == y)  # True because values are equal
print("x is y:", x is y)  # May be False because they may be different objects

# For small integers and short strings, Python often reuses the same object
small_a = 5
small_b = 5
print("small_a == small_b:", small_a == small_b)
print("small_a is small_b:", small_a is small_b)  # Often True for small integers

# Mutable objects usually have different identities even when equal
list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("list_a == list_b:", list_a == list_b)  # True because contents are equal
print("list_a is list_b:", list_a is list_b)  # False because they are different objects

# You can check the memory address of an object using id()
print("id(list_a):", id(list_a))
print("id(list_b):", id(list_b))

# Aliasing example: two names refer to the same mutable object
list_c = list_a
print("list_c is list_a:", list_c is list_a)  # True because list_c and list_a are same object
list_c.append(4)
print("list_a after modifying list_c:", list_a)

# ============================================================
# 3. VARIABLE SCOPE LAYERS
# ============================================================
# Scope determines where a variable name is visible and accessible.
# Common scopes: local, enclosing, global, built-in.

print("\n--- Variable Scope Layers ---")

global_var = "I am global"

def outer_function():
    enclosing_var = "I am enclosing"

    def inner_function():
        local_var = "I am local"
        print("Inside inner_function:")
        print("local_var:", local_var)
        print("enclosing_var:", enclosing_var)
        print("global_var:", global_var)

    inner_function()

outer_function()

# Global scope example
print("Global var outside functions:", global_var)

# Using global and nonlocal keywords
count = 0

def modify_global():
    global count
    count += 1
    print("Inside modify_global, count:", count)

modify_global()


def outer_counter():
    counter = 0

    def inner_counter():
        nonlocal counter
        counter += 1
        return counter

    print("First call:", inner_counter())
    print("Second call:", inner_counter())

outer_counter()

# ============================================================
# 4. GARBAGE COLLECTION BASICS
# ============================================================
# Python uses reference counting and a garbage collector to free memory.
# Objects are removed when nothing references them anymore.

print("\n--- Garbage Collection Basics ---")

import gc
print("Garbage collector enabled:", gc.isenabled())

# Create an object and multiple references to it
obj = [1, 2, 3]
ref1 = obj
ref2 = obj
print("Reference count example:")
print("id(obj):", id(obj))
print("obj == ref1:", obj == ref1)
print("obj is ref1:", obj is ref1)

# Delete one reference
print("Deleting ref1")
del ref1
# Object still exists because ref2 still points to it
print("obj is ref2 after deleting ref1:", obj is ref2)

# Delete the last reference
print("Deleting obj and ref2")
del obj

del ref2
# At this point the list object is eligible for garbage collection.

# Force a garbage collection cycle (usually not needed in normal code)
gc.collect()
print("Forced garbage collection run completed.")

# NOTE: Objects with circular references can still be collected by gc.
# Example of a circular reference:

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # circular reference

print("\nCircular reference example created")
print("node1 points to node2 and node2 points back to node1")

# Removing the names also makes the circular objects collectible
node1_id = id(node1)
node2_id = id(node2)
del node1
# remove the last reference name
node2 = None
gc.collect()
print("Garbage collection after removing circular references completed.")
print("Note: circular references can be collected by Python's gc module.")

# ============================================================
# 5. KEY TAKEAWAYS
# ============================================================
print("\n=== Key Takeaways ===")
print("- Mutable objects can change their contents; immutable objects cannot.")
print("- '==' compares values; 'is' compares object identity.")
print("- Scope defines where names are visible: local, enclosing, global, built-in.")
print("- Python uses reference counting plus a garbage collector for memory management.")
print("- Circular references are handled by the garbage collector when normal reference counting is not enough.")
