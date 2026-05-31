# Python Exceptions and Modules Basics
# This file covers exception bubbling and control flow, how imports resolve,
# absolute vs relative imports, and the global entrypoint.

# ============================================================
# 1. EXCEPTION BUBBLING AND CONTROL
# ============================================================
# Exceptions are raised when an error occurs. They bubble up the call stack
# until a matching except block catches them.

print("--- Exception Bubbling and Control ---")


def divide(a, b):
    print("Inside divide()")
    return a / b


def calculate():
    print("Inside calculate()")
    result = divide(10, 0)  # This will raise ZeroDivisionError
    print("This line is never reached")
    return result

try:
    calculate()
except ZeroDivisionError as error:
    print("Caught a ZeroDivisionError:", error)
except Exception as error:
    print("Caught a generic exception:", error)
else:
    print("No exception occurred")
finally:
    print("Finally block always runs")

print()

# Raising exceptions manually

def get_positive_number(value):
    if value <= 0:
        raise ValueError("Only positive numbers are allowed")
    return value

try:
    get_positive_number(-5)
except ValueError as error:
    print("Raised and caught ValueError:", error)

print()

# Exception bubbling with nested function calls

def inner():
    raise KeyError("missing-key")


def outer():
    print("Entering outer()")
    inner()
    print("Leaving outer()")

try:
    outer()
except KeyError as error:
    print("Caught KeyError from nested call:", error)

print("After outer() catch")

# ============================================================
# 2. IMPORT RESOLUTION MECHANICS
# ============================================================
# Python finds modules using the import system and sys.path list.
# It first checks built-in modules, then the current directory,
# then paths listed in PYTHONPATH and standard library directories.

print("\n--- Import Resolution Mechanics ---")

import sys
print("sys.path (first entries):")
for path in sys.path[:5]:
    print(" ", path)

print("\nBuilt-in modules can be imported without file paths:")
import math
print("math.sqrt(16)=", math.sqrt(16))

# If there is a local package or module with the same name it can shadow standard libraries,
# so use unique names for your own modules.

# Example: custom module resolution is based on package and script location.
# If you have a package, Python will try to load modules from package directories.

# ============================================================
# 3. ABSOLUTE VS RELATIVE IMPORTS
# ============================================================
# Absolute imports refer to the full package path.
# Relative imports use dots to navigate the package structure.

print("\n--- Absolute vs Relative Imports ---")

print("Use absolute imports when you want to import from the top-level package.")
print("Use relative imports inside packages to refer to sibling or parent modules.")

# Example package structure (not actual files in this script):
# mypackage/
#   __init__.py
#   helpers.py
#   tools/
#     __init__.py
#     formatter.py
#     parser.py
#
# Absolute import from formatter.py:
# from mypackage.tools.parser import parse_text
#
# Relative import from formatter.py to parser.py:
# from .parser import parse_text
#
# Relative import from tools/package to sibling module:
# from ..helpers import helper_function

print("Absolute import example:")
print("  from mypackage.tools.parser import parse_text")
print("Relative import example:")
print("  from .parser import parse_text")
print("  from ..helpers import helper_function")

# Relative imports only work inside packages, not from a top-level script.

# ============================================================
# 4. GLOBAL ENTRYPOINT
# ============================================================
# The global entrypoint is the code that runs when a script is executed.
# Use if __name__ == '__main__' to make code run only when a file is executed directly,
# not when it is imported as a module.

print("\n--- Global Entrypoint ---")


def main():
    print("This is the main() function.")
    print("The script is running directly.")


print("Top-level code always runs when the module is imported or executed.")

if __name__ == '__main__':
    main()
    print("__name__ is __main__, so this block runs.")
else:
    print("Module was imported, so __main__ block does not run.")

# ============================================================
# 5. SUMMARY
# ============================================================
print("\n=== Summary ===")
print("- Exceptions bubble up until caught by a matching except block.")
print("- try/except/else/finally controls how exceptions are handled.")
print("- Python resolves imports using sys.path and package structure.")
print("- Absolute imports use full package names, relative imports use dots.")
print("- Use if __name__ == '__main__' for the global program entrypoint.")
