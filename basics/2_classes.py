# Python Classes and Objects Tutorial
# This file covers object-oriented programming (OOP) fundamentals in Python

# ============================================================
# 1. WHAT ARE CLASSES AND OBJECTS?
# ============================================================
# A class is a blueprint or template for creating objects
# An object is an instance (a specific example) of a class
# 
# Think of it like this:
# - A class is like a recipe for making cookies
# - An object is an actual cookie made from that recipe
# - Each cookie is slightly different but follows the same recipe

# ============================================================
# 2. CREATING A SIMPLE CLASS
# ============================================================
# To create a class, use the 'class' keyword

class Dog:
    """A simple class representing a dog"""
    
    # These are attributes - properties that describe the object
    species = "Canis familiaris"  # This is a CLASS attribute (shared by all dogs)

# Creating objects (instances) from the Dog class
# We create a dog by calling the class name like a function
dog1 = Dog()
dog2 = Dog()

print("dog1 is an instance of Dog:", isinstance(dog1, Dog))
print("dog2 is an instance of Dog:", isinstance(dog2, Dog))

# ============================================================
# 3. THE __init__ METHOD (CONSTRUCTOR)
# ============================================================
# The __init__ method is called when you create a new object
# It initializes the object's attributes (properties)
# It's like the "setup" for a new object
# Methods in a class start and end with double underscores (__)

class Person:
    """A class representing a person"""
    
    def __init__(self, name, age):
        # 'self' represents the object itself
        # self.name creates an instance attribute called 'name'
        # Instance attributes are unique to each object
        self.name = name
        self.age = age
        self.email = None  # Initialize with None (no value yet)

# Create a person object
# When we do this, __init__ is automatically called
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print("\n--- Person Objects ---")
print(f"Person 1: {person1.name}, Age: {person1.age}")
print(f"Person 2: {person2.name}, Age: {person2.age}")

# ============================================================
# 4. ACCESSING AND MODIFYING ATTRIBUTES
# ============================================================
# You can access object attributes using dot notation: object.attribute
# You can also modify them the same way

print("\n--- Modifying Attributes ---")
print(f"Before: {person1.name} is {person1.age} years old")

# Modify an attribute
person1.age = 31
print(f"After: {person1.name} is {person1.age} years old")

# Set the email that was initially None
person1.email = "alice@email.com"
print(f"Email: {person1.email}")

# ============================================================
# 5. METHODS (FUNCTIONS INSIDE CLASSES)
# ============================================================
# Methods are functions defined inside a class
# They describe what objects of that class can do
# The first parameter is always 'self'

class Car:
    """A class representing a car"""
    
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.speed = 0  # Cars start at 0 speed
    
    # A method that doesn't change the object (just returns info)
    def describe(self):
        return f"A {self.color} {self.brand} car"
    
    # A method that changes the object's state
    def accelerate(self):
        self.speed += 10
        print(f"Accelerating! Speed is now {self.speed} mph")
    
    # A method with parameters
    def change_color(self, new_color):
        self.color = new_color
        print(f"Car color changed to {self.color}")

# Create car objects
print("\n--- Car Objects and Methods ---")
car1 = Car("Toyota", "blue")
car2 = Car("Honda", "red")

# Call methods on objects
print(car1.describe())  # Calls the describe method
print(car2.describe())

# Call methods that change the object
car1.accelerate()  # Speed goes from 0 to 10
car1.accelerate()  # Speed goes from 10 to 20
car1.accelerate()  # Speed goes from 20 to 30

# Call method with parameters
car1.change_color("green")

# ============================================================
# 6. CLASS ATTRIBUTES VS INSTANCE ATTRIBUTES
# ============================================================
# Class attributes: shared by all instances of the class
# Instance attributes: unique to each object

class Book:
    """A class representing a book"""
    
    # Class attribute - same for all books
    medium = "paper"  # Could be "digital" too, but default is "paper"
    
    def __init__(self, title, author, pages):
        # Instance attributes - different for each book
        self.title = title
        self.author = author
        self.pages = pages

print("\n--- Class vs Instance Attributes ---")
book1 = Book("Python Basics", "John Doe", 300)
book2 = Book("Web Development", "Jane Smith", 450)

# Accessing instance attributes
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")

# Accessing class attributes (same for both)
print(f"Book 1 medium: {book1.medium}")
print(f"Book 2 medium: {book2.medium}")

# Change class attribute (affects all instances)
Book.medium = "digital"
print(f"\nAfter changing class attribute:")
print(f"Book 1 medium: {book1.medium}")
print(f"Book 2 medium: {book2.medium}")

# ============================================================
# 7. MORE COMPLEX EXAMPLE: BANK ACCOUNT
# ============================================================
# A more practical example combining multiple concepts

class BankAccount:
    """A class representing a bank account"""
    
    bank_name = "Python Bank"  # Class attribute
    
    def __init__(self, account_holder, initial_balance=0):
        # Instance attributes
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []  # List to track transactions
    
    def deposit(self, amount):
        """Add money to the account"""
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        """Remove money from the account"""
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive")
    
    def get_balance(self):
        """Return the current balance"""
        return self.balance
    
    def get_account_info(self):
        """Return account information"""
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
    
    def show_transactions(self):
        """Display all transactions"""
        print(f"\nTransactions for {self.account_holder}:")
        for transaction in self.transactions:
            print(f"  - {transaction}")

# Create bank accounts
print("\n--- Bank Account Example ---")
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob", 500)

# Use the account methods
account1.deposit(200)
account1.withdraw(150)
account1.deposit(300)
account1.withdraw(100)

print(f"\n{account1.get_account_info()}")
account1.show_transactions()

account2.deposit(100)
account2.withdraw(600)  # This will show insufficient funds
account2.withdraw(200)

print(f"\n{account2.get_account_info()}")
account2.show_transactions()

# ============================================================
# 8. SPECIAL METHODS (DUNDER METHODS)
# ============================================================
# Special methods start and end with double underscores
# They define how objects behave with Python's built-in operations

class Student:
    """A class representing a student"""
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    # __str__ defines what print() shows
    def __str__(self):
        return f"Student: {self.name} (Grade: {self.grade})"
    
    # __repr__ defines what appears in the console
    def __repr__(self):
        return f"Student('{self.name}', '{self.grade}')"
    
    # __len__ allows len() to work on your object
    def __len__(self):
        return len(self.name)
    
    # __eq__ allows comparison with ==
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.name == other.name and self.grade == other.grade
        return False

print("\n--- Special Methods ---")
student1 = Student("Charlie", "A")
student2 = Student("Diana", "B")
student3 = Student("Charlie", "A")

# __str__ is used by print()
print(student1)  # Uses __str__

# __len__ allows len()
print(f"Length of student name: {len(student1)}")

# __eq__ allows comparison
print(f"student1 == student2: {student1 == student2}")  # False
print(f"student1 == student3: {student1 == student3}")  # True

# ============================================================
# 9. INHERITANCE (BASICS)
# ============================================================
# Inheritance allows one class to inherit attributes and methods from another
# The parent class is called the superclass
# The child class is called the subclass

class Animal:
    """Parent class"""
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog2(Animal):
    """Child class that inherits from Animal"""
    # Override the speak method
    def speak(self):
        return f"{self.name} barks: Woof!"

class Cat(Animal):
    """Another child class"""
    def speak(self):
        return f"{self.name} meows: Meow!"

print("\n--- Inheritance Example ---")
dog = Dog2("Rex")
cat = Cat("Whiskers")

print(dog.speak())  # Uses Dog's speak method
print(cat.speak())  # Uses Cat's speak method

# ============================================================
# 10. SUMMARY AND KEY CONCEPTS
# ============================================================
print("\n=== KEY CONCEPTS SUMMARY ===")
print("1. Classes are blueprints for creating objects")
print("2. Objects are instances created from classes")
print("3. __init__ method initializes new objects")
print("4. 'self' refers to the object itself")
print("5. Instance attributes are unique to each object")
print("6. Class attributes are shared by all objects")
print("7. Methods are functions that belong to objects")
print("8. Special methods (dunder methods) define object behavior")
print("9. Inheritance allows classes to inherit from other classes")
print("10. Objects can be modified by calling their methods or changing attributes")

print("\n=== End of Classes and Objects Tutorial ===")
