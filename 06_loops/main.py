# =============================================================
#  MODULE 06 — LOOPS
#  Level: [OK] Beginner
#  Goal:  Repeat actions using for, while, break, continue.
# =============================================================

print("=" * 55)
print("  MODULE 06 — LOOPS")
print("=" * 55)

# ----- 1. FOR LOOP BASICS -----
print("\n--- 1. For Loop Basics ---")
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(f"    [*] {color}")

for letter in "PYTHON":
    print(f"    -> {letter}")

# ----- 2. RANGE() FUNCTION -----
print("\n--- 2. range() ---")
print("  range(5)        ->", list(range(5)))
print("  range(2, 8)     ->", list(range(2, 8)))
print("  range(0, 20, 3) ->", list(range(0, 20, 3)))

print("\n  [math] Multiplication Table for 7:")
for i in range(1, 11):
    print(f"    7 × {i:2d} = {7 * i:3d}")

# ----- 3. ENUMERATE() -----
print("\n--- 3. enumerate() ---")
languages = ["Python", "JavaScript", "Rust", "Go"]
for rank, lang in enumerate(languages, start=1):
    print(f"    #{rank} {lang}")

# ----- 4. WHILE LOOP -----
print("\n--- 4. While Loop ---")
count = 5
while count > 0:
    print(f"    {count}...")
    count -= 1
print("    !! Liftoff!")

# ----- 5. BREAK AND CONTINUE -----
print("\n--- 5. break & continue ---")
for n in range(1, 100):
    if n % 7 == 0:
        print(f"  First divisible by 7: {n}")
        break

print("  Odd numbers 1-10:", end=" ")
for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# ----- 6. FOR...ELSE -----
print("\n--- 6. for...else ---")
target = 42
for num in [10, 23, 35, 42, 58]:
    if num == target:
        print(f"  [OK] Found {target}!")
        break
else:
    print(f"  [X] {target} not found.")

# ----- 7. NESTED LOOPS -----
print("\n--- 7. Nested Loops ---")
for row in range(1, 6):
    print("    " + "*" * row)

# ----- 8. ZIP() -----
print("\n--- 8. zip() ---")
names = ["Alice", "Bob", "Charlie"]
scores = [95, 82, 91]
for name, score in zip(names, scores):
    print(f"    [doc] {name:<10} Score: {score}")

# ----- 9. COMMON PATTERNS -----
print("\n--- 9. Common Patterns ---")
nums = [4, 7, 2, 9, 1]
print(f"  Sum of {nums} = {sum(nums)}")

original = [1, 2, 3, 4, 5]
squared = []
for n in original:
    squared.append(n ** 2)
print(f"  Squares: {squared}")

# ----- MINI CHALLENGE -----
print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES: FizzBuzz, Prime finder, Star patterns")
print("=" * 55)
