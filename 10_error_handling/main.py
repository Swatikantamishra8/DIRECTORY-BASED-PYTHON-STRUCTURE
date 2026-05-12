# =============================================================
#  MODULE 10 — ERROR HANDLING
#  Level: [WARN] Intermediate
#  Goal:  Handle errors gracefully, create custom exceptions.
# =============================================================

import logging

print("=" * 55)
print("  MODULE 10 — ERROR HANDLING")
print("=" * 55)

# ----- 1. BASIC TRY / EXCEPT -----
print("\n--- 1. Basic try / except ---")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("  [X] Cannot divide by zero!")

try:
    num = int("hello")
except ValueError:
    print("  [X] 'hello' is not a valid number!")

# ----- 2. MULTIPLE EXCEPT BLOCKS -----
print("\n--- 2. Multiple except blocks ---")

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid types"

print(f"  10 / 3     = {safe_divide(10, 3)}")
print(f"  10 / 0     = {safe_divide(10, 0)}")
print(f"  10 / 'abc' = {safe_divide(10, 'abc')}")

# ----- 3. TRY / EXCEPT / ELSE / FINALLY -----
print("\n--- 3. try / except / else / finally ---")

try:
    value = int("42")
except ValueError:
    print("  [X] Conversion failed")
else:
    print(f"  [OK] Conversion succeeded: {value}")
finally:
    print("  [~] This ALWAYS runs (cleanup goes here).")

# ----- 4. RAISING EXCEPTIONS -----
print("\n--- 4. Raising Exceptions ---")

def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age seems unrealistic: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"  Caught: {e}")

# ----- 5. CUSTOM EXCEPTIONS -----
print("\n--- 5. Custom Exceptions ---")

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"Cannot withdraw Rs.{amount}. Balance: Rs.{balance}"
        )

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(500, 1000)
except InsufficientFundsError as e:
    print(f"  Caught custom error: {e}")

# ----- 6. COMMON EXCEPTION TYPES -----
print("\n--- 6. Common Exception Types ---")
exceptions = {
    "ValueError":      "Wrong value type (e.g., int('abc'))",
    "TypeError":       "Wrong operation for type (e.g., '2' + 2)",
    "IndexError":      "List index out of range",
    "KeyError":        "Dict key not found",
    "FileNotFoundError": "File doesn't exist",
    "AttributeError":  "Object has no such attribute",
    "ImportError":     "Module not found",
    "ZeroDivisionError": "Division by zero",
}
for exc, desc in exceptions.items():
    print(f"    {exc:<22} -> {desc}")

# ----- 7. LOGGING (production-grade error handling) -----
print("\n--- 7. Logging (Preview) ---")
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.debug("This is debug (won't show at INFO level)")
logging.info("Application started successfully")
logging.warning("Disk space is running low")
logging.error("Failed to connect to database")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a safe calculator that never crashes")
print("  2. Create a file reader that handles missing files")
print("  3. Build a user registration with input validation")
print("=" * 55)
