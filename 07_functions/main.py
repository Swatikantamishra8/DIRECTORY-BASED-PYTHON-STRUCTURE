# =============================================================
#  MODULE 07 — FUNCTIONS
#  Level: [WARN] Intermediate
#  Goal:  Define reusable blocks of code. Master parameters,
#         return values, scope, *args, **kwargs, lambda.
# =============================================================

print("=" * 55)
print("  MODULE 07 — FUNCTIONS")
print("=" * 55)

# ----- 1. BASIC FUNCTION -----
print("\n--- 1. Basic Function ---")

def greet(name):
    """Greet a person by name."""
    print(f"    Hello, {name}! Welcome to Python.")

greet("Swati")
greet("World")

# ----- 2. RETURN VALUES -----
print("\n--- 2. Return Values ---")

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

result = add(10, 25)
print(f"  add(10, 25) = {result}")
print(f"  is_even(7) = {is_even(7)}")
print(f"  is_even(8) = {is_even(8)}")

# Returning multiple values (as a tuple)
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([4, 9, 1, 7, 3])
print(f"  Min: {low}, Max: {high}")

# ----- 3. DEFAULT PARAMETERS -----
print("\n--- 3. Default Parameters ---")

def power(base, exponent=2):
    return base ** exponent

print(f"  power(5)    = {power(5)}")      # Uses default exponent=2
print(f"  power(5, 3) = {power(5, 3)}")   # Overrides to 3

# ----- 4. *ARGS AND **KWARGS -----
print("\n--- 4. *args and **kwargs ---")

# *args — Accept any number of positional arguments
def total(*args):
    print(f"    Received: {args}")
    return sum(args)

print(f"  total(1,2,3) = {total(1, 2, 3)}")

# **kwargs — Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print("  User info:")
print_info(name="Swati", role="Developer", lang="Python")

# ----- 5. SCOPE — LOCAL vs GLOBAL -----
print("\n--- 5. Variable Scope ---")

global_var = "I'm global"

def scope_demo():
    local_var = "I'm local"
    print(f"    Inside function: {global_var}")
    print(f"    Inside function: {local_var}")

scope_demo()
print(f"    Outside function: {global_var}")
# print(local_var)  <- This would cause NameError!

# ----- 6. LAMBDA FUNCTIONS -----
print("\n--- 6. Lambda (Anonymous Functions) ---")

square = lambda x: x ** 2
add_two = lambda a, b: a + b

print(f"  square(9)     = {square(9)}")
print(f"  add_two(3, 7) = {add_two(3, 7)}")

# Lambda with sorted()
students = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(f"  Sorted by score: {by_score}")

# ----- 7. HIGHER-ORDER FUNCTIONS -----
print("\n--- 7. map(), filter(), reduce() ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled = list(map(lambda x: x * 2, numbers))
print(f"  Doubled: {doubled}")

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Evens:   {evens}")

from functools import reduce
product = reduce(lambda a, b: a * b, numbers)
print(f"  Product: {product}")

# ----- 8. RECURSION -----
print("\n--- 8. Recursion ---")

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"  5! = {factorial(5)}")
print(f"  Fibonacci(10) = {fibonacci(10)}")

# ----- 9. DOCSTRINGS & TYPE HINTS -----
print("\n--- 9. Type Hints & Docstrings ---")

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate Body Mass Index.

    Args:
        weight_kg: Weight in kilograms.
        height_m:  Height in meters.

    Returns:
        BMI as a float.
    """
    return round(weight_kg / (height_m ** 2), 1)

bmi = calculate_bmi(70, 1.75)
print(f"  BMI(70kg, 1.75m) = {bmi}")
print(f"  Docstring: {calculate_bmi.__doc__[:40]}...")

# ----- MINI CHALLENGE -----
print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Write a function that checks if a string is a palindrome")
print("  2. Write a recursive function for sum of digits")
print("  3. Create a password validator function")
print("=" * 55)
