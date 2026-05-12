# =============================================================
#  MODULE 05 — CONTROL FLOW
#  Level: [OK] Beginner
#  Goal:  Make decisions in code using if/elif/else, ternary,
#         and match-case (Python 3.10+).
# =============================================================

print("=" * 55)
print("  MODULE 05 — CONTROL FLOW")
print("=" * 55)

# ----- 1. BASIC IF / ELSE -----
print("\n--- 1. Basic if / else ---")

temperature = 35

if temperature > 30:
    print(f"  (!) {temperature}°C — It's HOT outside!")
else:
    print(f"  ❄️ {temperature}°C — It's cool outside.")


# ----- 2. IF / ELIF / ELSE -----
# Use elif when you have more than 2 outcomes.
print("\n--- 2. if / elif / else (Grade Calculator) ---")

score = 82

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"  Score: {score} -> Grade: {grade}")


# ----- 3. NESTED IF -----
print("\n--- 3. Nested if ---")

age = 22
has_license = True

if age >= 18:
    if has_license:
        print("  [OK] You can drive!")
    else:
        print("  [!] You're old enough, but need a license first.")
else:
    print("  [X] You're too young to drive.")


# ----- 4. LOGICAL OPERATORS IN CONDITIONS -----
print("\n--- 4. Combining Conditions (and, or, not) ---")

username = "admin"
password = "secret123"

if username == "admin" and password == "secret123":
    print("  [OK] Login successful!")
else:
    print("  [X] Invalid credentials.")

day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print(f"  !! {day} is a weekend — relax!")
else:
    print(f"  💼 {day} is a workday.")

is_raining = False
if not is_raining:
    print("  (sun) No rain — go for a walk!")


# ----- 5. TERNARY (ONE-LINE IF) -----
# Format: value_if_true IF condition ELSE value_if_false
print("\n--- 5. Ternary Operator (One-liner) ---")

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"  Age {age} -> {status}")

number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(f"  Number {number} -> {parity}")


# ----- 6. TRUTHY AND FALSY VALUES -----
# In Python, some values are "falsy" (treated as False):
# False, 0, 0.0, "", [], {}, (), None
# Everything else is "truthy".
print("\n--- 6. Truthy & Falsy Values ---")

values = [0, 1, "", "hello", [], [1, 2], None, True, False, {}, {"key": "val"}]

for val in values:
    label = "Truthy [OK]" if val else "Falsy  [X]"
    print(f"  {str(val):>15} -> {label}")


# ----- 7. MATCH-CASE (Python 3.10+) -----
# Structural pattern matching — Python's version of switch/case.
print("\n--- 7. Match-Case (Python 3.10+) ---")

command = "start"

match command:
    case "start":
        print("  [OK] Starting the engine...")
    case "stop":
        print("  [ERR] Stopping the engine...")
    case "pause":
        print("  [WARN] Pausing the engine...")
    case _:
        print(f"  [?] Unknown command: {command}")

# Match-case with patterns
print("\n  Match-case with tuple patterns:")

point = (0, 5)

match point:
    case (0, 0):
        print(f"  {point} -> Origin")
    case (0, y):
        print(f"  {point} -> On Y-axis at y={y}")
    case (x, 0):
        print(f"  {point} -> On X-axis at x={x}")
    case (x, y):
        print(f"  {point} -> Point at ({x}, {y})")


# ----- 8. REAL-WORLD EXAMPLE: Simple ATM -----
print("\n--- 8. Real-World Example: Mini ATM ---")

balance = 5000.00
print(f"  $ Current Balance: Rs.{balance:.2f}")

action = "withdraw"   # Change this to "deposit" or "check" to test
amount = 1500

if action == "check":
    print(f"  [i] Your balance is Rs.{balance:.2f}")
elif action == "deposit":
    balance += amount
    print(f"  [OK] Deposited Rs.{amount}. New balance: Rs.{balance:.2f}")
elif action == "withdraw":
    if amount > balance:
        print(f"  [X] Insufficient funds! You only have Rs.{balance:.2f}")
    else:
        balance -= amount
        print(f"  [OK] Withdrew Rs.{amount}. New balance: Rs.{balance:.2f}")
else:
    print(f"  [?] Unknown action: {action}")


# ----- MINI CHALLENGE -----
print("\n" + "=" * 55)
print("  [TROPHY] MINI CHALLENGES")
print("=" * 55)
print("  1. Build a traffic light system (red/yellow/green)")
print("  2. Create a BMI calculator with health categories")
print("  3. Make an eligibility checker (voting, driving, etc.)")
print("  4. Write a rock-paper-scissors logic (no loops yet!)")
print("=" * 55)
