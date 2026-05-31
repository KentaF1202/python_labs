# Python Functional Basics: First-Class Functions, Closures, Decorators, and Generators
# This file explains how Python treats functions like variables,
# how closures and decorators work, and how generators produce values lazily.

# ============================================================
# 1. FIRST-CLASS FUNCTIONS
# ============================================================
# In Python, functions are first-class objects.
# That means functions can be stored in variables, passed as arguments,
# returned from other functions, and stored in data structures.

print("--- First-Class Functions ---")

# Assigning a function to a variable


def greet():
    print("Hello!")


say_hello = greet  # function object assigned to a variable
say_hello()  # call the function through the new name

# Passing a function as an argument


def run_twice(func):
    func()
    func()


run_twice(greet)

# Returning a function from another function


def make_multiplier(factor):
    def multiply(value):
        return value * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print("double(5):", double(5))
print("triple(5):", triple(5))

# Storing functions in a list

functions = [greet, lambda: print("Goodbye!"), double]
for fn in functions:
    if fn.__name__ == "multiply":
        print("double(3) from list:", fn(3))
    else:
        fn()

# ============================================================
# 2. CLOSURES
# ============================================================
# A closure is a function that remembers values from its enclosing scope,
# even after the outer function has finished executing.

print("\n--- Closures ---")


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter_a = make_counter()
print("counter_a():", counter_a())
print("counter_a():", counter_a())

counter_b = make_counter()
print("counter_b():", counter_b())  # separate closure with its own state

# Another closure example: creating a personalized greeter


def make_greeter(name):
    def greeter():
        print(f"Hello, {name}!")

    return greeter


alice_greeter = make_greeter("Alice")
alice_greeter()

# ============================================================
# 3. DECORATORS
# ============================================================
# A decorator is a function that wraps another function,
# adding behavior before or after it runs.
# The @ syntax is a convenient shorthand for applying decorators.

print("\n--- Decorators ---")


def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before calling", func.__name__)
        result = func(*args, **kwargs)
        print("After calling", func.__name__)
        return result

    return wrapper


@simple_decorator
def say_goodbye():
    print("Goodbye!")


say_goodbye()

# Decorator with arguments and return value


def timer_decorator(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result

    return wrapper


@timer_decorator
def compute_sum(n):
    return sum(range(n))


print("compute_sum(1000000):", compute_sum(1000000))

# Decorators can be applied manually too


def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def say_name(name):
    return f"Hello, {name}"


say_name = uppercase_decorator(say_name)
print(say_name("Alice"))

# ============================================================
# 4. GENERATORS
# ============================================================
# Generators use the yield keyword to produce values one at a time.
# They are useful for lazy iteration and large data flows.

print("\n--- Generators ---")


def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


for number in count_up_to(5):
    print(number)

# Generators can be iterated with next()

counter = count_up_to(3)
print("next(counter):", next(counter))
print("next(counter):", next(counter))
print("next(counter):", next(counter))
# next(counter) would raise StopIteration after the generator is exhausted

# Generator expression: a compact way to create a generator

squares = (x * x for x in range(1, 6))
print("Generator expression squares type:", type(squares))
print("Squares:", list(squares))

# Generators are memory-efficient because they produce values on demand

large_gen = (i for i in range(1000000))
print("First value from large_gen:", next(large_gen))
print("Second value from large_gen:", next(large_gen))

# ============================================================
# 5. SUMMARY
# ============================================================
print("\n=== Summary ===")
print("- Functions are first-class objects in Python.")
print("- Closures let functions remember state from their enclosing scope.")
print("- Decorators wrap functions to add extra behavior.")
print("- Generators produce values lazily using yield.")
