# Python Dunder Methods and Protocols Tutorial
# This file explains object representation, the iterator protocol,
# context managers, and operator overloading.

# ============================================================
# 1. OBJECT REPRESENTATION
# ============================================================
# __str__ and __repr__ control how objects appear when printed or
# inspected in the console.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        # __repr__ should return an unambiguous representation
        return f"Product(name={self.name!r}, price={self.price!r})"

    def __str__(self):
        # __str__ should return a readable representation for users
        return f"{self.name} costs ${self.price:.2f}"

p = Product("Laptop", 999.99)
print("--- Object Representation ---")
print("repr:", repr(p))
print("str:", str(p))
print("print directly:", p)

# ============================================================
# 2. ITERATOR PROTOCOL
# ============================================================
# Python objects can be made iterable by implementing __iter__ and __next__.
# __iter__ returns the iterator object, and __next__ returns the next value.

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        # Return the iterator object itself
        return self

    def __next__(self):
        # Return the next value or raise StopIteration when done
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("\n--- Iterator Protocol ---")
for number in Countdown(5):
    print(number)

# We can also manually use next() with the iterator
count = Countdown(3)
iterator = iter(count)
print("Manual iteration:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
# next(iterator) would raise StopIteration here if called again

# ============================================================
# 3. CONTEXT MANAGERS
# ============================================================
# Context managers implement __enter__ and __exit__.
# They are used with the 'with' statement to set up and tear down resources.

class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Open the file when entering the with-block
        self.file = open(self.filename, "w")
        print("Opening file")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        # Close the file when exiting the with-block
        if self.file:
            self.file.close()
            print("Closing file")
        # Return False to propagate exceptions, True to suppress them
        return False

print("\n--- Context Manager ---")
with FileWriter("sample.txt") as f:
    f.write("Hello from a context manager!\n")

print("File context block completed.")

# A simple context manager for timing operations
import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        elapsed = self.end - self.start
        print(f"Elapsed time: {elapsed:.4f} seconds")

print("\n--- Timing Context Manager ---")
with Timer():
    total = sum(range(1000000))
    print("Sum calculation complete")

# ============================================================
# 4. OPERATOR OVERLOADING
# ============================================================
# Operator overloading means defining how objects behave with operators
# like +, -, *, ==, and more. These are controlled by dunder methods.

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector2D(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector2D(2, 3)
v2 = Vector2D(4, 1)
print("\n--- Operator Overloading ---")
print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v1 + v2)
print("v1 * 3:", v1 * 3)
print("v1 == v2:", v1 == v2)
print("v1 == Vector2D(2, 3):", v1 == Vector2D(2, 3))

# ============================================================
# 5. SUMMARY
# ============================================================
print("\n=== Summary ===")
print("- __repr__ and __str__ control object printing and inspection.")
print("- __iter__ and __next__ make objects iterable in loops.")
print("- __enter__ and __exit__ define context manager behavior for with.")
print("- Operator overloading lets objects work with +, *, ==, and more.")
print("- Dunder methods make custom objects behave like built-in types.")
