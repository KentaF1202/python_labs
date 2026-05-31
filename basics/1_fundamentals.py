# Python Basics Tutorial
# This file covers the fundamental concepts you need to start coding in Python

# ============================================================
# 1. COMMENTS
# ============================================================
# A comment is a line of text that Python ignores. It helps explain your code.
# Comments start with a # symbol
# They are useful for explaining what your code does

# You can also use multi-line comments with triple quotes:
"""
This is a multi-line comment.
It can span multiple lines.
Useful for longer explanations or documentation.
"""

# ============================================================
# 2. PRINT STATEMENTS
# ============================================================
# print() displays text or values to the screen
# This is the first time we're using print, so here's what it does:
# - It takes whatever you put inside the parentheses
# - It shows it on the screen
# - Then it moves to the next line

print("Hello, World!")  # This prints the text "Hello, World!"
print("Welcome to Python!")  # This prints another message

# You can also print numbers and other values
print(42)  # Print the number 42
print(3.14)  # Print a decimal number

# ============================================================
# 3. VARIABLES
# ============================================================
# A variable is a container that stores a value
# Think of it like a labeled box that holds information
# You create a variable by giving it a name and a value

# Creating variables with different types of data:
name = "Alice"  # A string (text) variable
age = 25  # An integer (whole number) variable
height = 5.6  # A float (decimal number) variable
is_student = True  # A boolean (True/False) variable

# Print the variables to see their values
print(name)  # Prints: Alice
print(age)  # Prints: 25

# You can also print multiple values in one print statement
print("Name:", name, "Age:", age)  # Prints: Name: Alice Age: 25

# Variables can be changed (that's why they're called "variables")
age = 26  # Now age holds the value 26
print("Updated age:", age)  # Prints: Updated age: 26

# ============================================================
# 4. INPUT STATEMENTS
# ============================================================
# input() lets the user type something into the program
# This is the first time we're using input, so here's how it works:
# - The program pauses and waits for the user to type something
# - The user types their answer and presses Enter
# - input() returns what they typed as a string (text)
# - We store it in a variable

# For demonstration, we'll show the concept (commented out so the tutorial runs without waiting for input)
# favorite_color = input("What is your favorite color? ")
# print("You like", favorite_color)

# ============================================================
# 5. IF STATEMENTS
# ============================================================
# An if statement lets you make decisions in your code
# It checks if something is True, and if it is, it runs that code block
# If it's False, it skips that code block

# Simple if example:
score = 85
if score >= 80:
    print("Great job! You passed!")  # This runs because 85 >= 80 is True

# Using if-else: run one block if True, another if False
age = 17
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")  # This prints because age is 17

# Using if-elif-else: check multiple conditions
grade = 92
if grade >= 90:
    print("Grade: A")
elif grade >= 80:  # elif means "else if"
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
else:
    print("Grade: F")  # This prints because 92 >= 90

# ============================================================
# 6. LOOPS
# ============================================================
# A loop repeats code multiple times
# There are two main types: for loops and while loops

# FOR LOOP: repeats a specific number of times
# The range(5) creates numbers 0, 1, 2, 3, 4
print("\n--- FOR LOOP EXAMPLE ---")
for i in range(5):
    print("Count:", i)  # This prints 5 times
# Output: Count: 0, Count: 1, Count: 2, Count: 3, Count: 4

# FOR LOOP with a list
print("\n--- FOR LOOP WITH A LIST ---")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print("I like", fruit)  # Repeats for each fruit in the list

# WHILE LOOP: repeats while a condition is True
# Keep repeating while counter < 3
print("\n--- WHILE LOOP EXAMPLE ---")
counter = 0
while counter < 3:
    print("Counter is:", counter)
    counter = counter + 1  # Increase counter by 1 each time
# Output: Counter is: 0, Counter is: 1, Counter is: 2

# ============================================================
# 7. FUNCTIONS
# ============================================================
# A function is a reusable block of code that performs a specific task
# You define a function once, then call it (use it) multiple times
# Functions help organize code and avoid repetition

# Defining a simple function (no inputs, no outputs)
def say_hello():
    print("Hello, friend!")

# Call the function (run it)
say_hello()  # This prints: Hello, friend!
say_hello()  # We can call it again

# Function with parameters (inputs)
# Parameters are values you pass to the function
def greet(name):
    print("Hello,", name + "!")

# Call the function with different values
greet("Alice")  # Prints: Hello, Alice!
greet("Bob")    # Prints: Hello, Bob!

# Function that returns a value (output)
# The return keyword sends a value back to whoever called the function
def add_numbers(a, b):
    result = a + b
    return result  # Send the result back

# Call the function and store the result in a variable
sum_result = add_numbers(5, 3)
print("5 + 3 =", sum_result)  # Prints: 5 + 3 = 8

# Function with multiple parameters and operations
def calculate_age(birth_year):
    current_year = 2024
    age = current_year - birth_year
    return age

my_age = calculate_age(2000)
print("Your age:", my_age)  # Prints: Your age: 24

# ============================================================
# 8. PUTTING IT ALL TOGETHER
# ============================================================
# Let's create a simple program that uses all these concepts

def welcome_user():
    """This function welcomes the user and demonstrates basic concepts"""
    print("\n=== Simple Calculator ===")
    
    # Get input from user (commented out for automatic running)
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    print(f"You entered: {num1} and {num2}")
    
    # If statement to check which number is bigger
    if num1 > num2:
        print(f"{num1} is bigger than {num2}")
    elif num2 > num1:
        print(f"{num2} is bigger than {num1}")
    else:
        print("Both numbers are equal")
    
    # Loop to show multiplication table
    print(f"\nMultiplication table of {num1}:")
    for i in range(1, 6):
        result = num1 * i
        print(f"{num1} × {i} = {result}")

# Call the function to run the complete example
welcome_user()

print("\n=== End of Python Basics ===")
print("Great job! You now understand the fundamentals of Python!")
