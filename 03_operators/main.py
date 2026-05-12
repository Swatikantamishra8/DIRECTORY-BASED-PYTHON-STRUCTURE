# =============================================================
#  MODULE 03 — OPERATORS
#  Level: [OK] Beginner
#  Goal:  Master every Python operator category.
# =============================================================

print("=" * 55)
print("  MODULE 03 — OPERATORS IN PYTHON")
print("=" * 55)

# ----- 1. ARITHMETIC OPERATORS -----
print("\n--- 1. Arithmetic Operators ---")

a, b = 17, 5

print(f"  a = {a}, b = {b}")
print(f"  a + b  = {a + b}")       # Addition
print(f"  a - b  = {a - b}")       # Subtraction
print(f"  a * b  = {a * b}")       # Multiplication
print(f"  a / b  = {a / b}")       # True Division (always returns float)
print(f"  a // b = {a // b}")      # Floor Division (rounds DOWN to integer)
print(f"  a % b  = {a % b}")       # Modulo (remainder)
print(f"  a ** b = {a ** b}")      # Exponentiation (a to the power of b)


# ----- 2. COMPARISON OPERATORS -----
# These always return True or False (a boolean).
print("\n--- 2. Comparison Operators ---")

x, y = 10, 20

print(f"  x = {x}, y = {y}")
print(f"  x == y -> {x == y}")    # Equal to
print(f"  x != y -> {x != y}")    # Not equal to
print(f"  x > y  -> {x > y}")     # Greater than
print(f"  x < y  -> {x < y}")     # Less than
print(f"  x >= y -> {x >= y}")    # Greater than or equal to
print(f"  x <= y -> {x <= y}")    # Less than or equal to


# ----- 3. LOGICAL OPERATORS -----
# Combine multiple conditions. Think of them as English words.
print("\n--- 3. Logical Operators ---")

is_sunny = True
is_warm = False

print(f"  is_sunny = {is_sunny}, is_warm = {is_warm}")
print(f"  is_sunny AND is_warm -> {is_sunny and is_warm}")  # Both must be True
print(f"  is_sunny OR  is_warm -> {is_sunny or is_warm}")   # At least one True
print(f"  NOT is_sunny         -> {not is_sunny}")           # Flips the value


# ----- 4. ASSIGNMENT OPERATORS -----
# Shortcuts for updating a variable's value.
print("\n--- 4. Assignment Operators ---")

score = 100
print(f"  Starting score: {score}")

score += 10   # Same as: score = score + 10
print(f"  score += 10 -> {score}")

score -= 25   # Same as: score = score - 25
print(f"  score -= 25 -> {score}")

score *= 2    # Same as: score = score * 2
print(f"  score *= 2  -> {score}")

score //= 3   # Same as: score = score // 3
print(f"  score //= 3 -> {score}")

score **= 2   # Same as: score = score ** 2
print(f"  score **= 2 -> {score}")


# ----- 5. IDENTITY OPERATORS -----
# "is" checks if two variables point to the EXACT same object in memory.
# This is different from == which checks VALUE equality.
print("\n--- 5. Identity Operators (is / is not) ---")

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a        # list_c points to the SAME object as list_a

print(f"  list_a == list_b -> {list_a == list_b}")   # True (same values)
print(f"  list_a is list_b -> {list_a is list_b}")   # False (different objects!)
print(f"  list_a is list_c -> {list_a is list_c}")   # True (same object)


# ----- 6. MEMBERSHIP OPERATORS -----
# Check if something exists inside a collection.
print("\n--- 6. Membership Operators (in / not in) ---")

fruits = ["apple", "banana", "mango"]
print(f"  fruits = {fruits}")
print(f"  'banana' in fruits     -> {'banana' in fruits}")
print(f"  'grape' not in fruits  -> {'grape' not in fruits}")


# ----- 7. BITWISE OPERATORS (Preview) -----
# These work on binary (0s and 1s). Useful in low-level programming.
print("\n--- 7. Bitwise Operators (Preview) ---")

p, q = 6, 3  # 6 = 110 in binary, 3 = 011 in binary
print(f"  p = {p} (binary: {bin(p)}), q = {q} (binary: {bin(q)})")
print(f"  p & q  (AND) = {p & q}")     # 010 = 2
print(f"  p | q  (OR)  = {p | q}")     # 111 = 7
print(f"  p ^ q  (XOR) = {p ^ q}")     # 101 = 5
print(f"  ~p     (NOT) = {~p}")        # Inverts all bits
print(f"  p << 1 (Left Shift)  = {p << 1}")   # 1100 = 12
print(f"  p >> 1 (Right Shift) = {p >> 1}")    # 011 = 3


# ----- 8. OPERATOR PRECEDENCE -----
# Python follows math order: Parentheses -> Exponent -> Mult/Div -> Add/Sub
print("\n--- 8. Operator Precedence ---")

expr1 = 2 + 3 * 4      # 3*4 first -> 12 + 2 = 14
expr2 = (2 + 3) * 4    # Parentheses first -> 5 * 4 = 20

print(f"  2 + 3 * 4   = {expr1}  (multiplication first)")
print(f"  (2 + 3) * 4 = {expr2}  (parentheses first)")

# TIP: When in doubt, use parentheses to make your intent crystal clear!


# ----- MINI CHALLENGE -----
print("\n" + "=" * 55)
print("  [TROPHY] MINI CHALLENGE")
print("=" * 55)
print("  Try modifying the code above!")
print("  1. What happens with negative numbers in floor division?")
print("  2. Can you use 'in' to check letters inside a string?")
print("  3. What is 2 ** 10? (Hint: it's a famous number in CS)")
print("=" * 55)
