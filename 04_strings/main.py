# =============================================================
#  MODULE 04 — STRINGS DEEP DIVE
#  Level: [OK] Beginner
#  Goal:  Master string creation, slicing, methods & formatting.
# =============================================================

print("=" * 55)
print("  MODULE 04 — STRINGS DEEP DIVE")
print("=" * 55)

# ----- 1. CREATING STRINGS -----
print("\n--- 1. Creating Strings ---")

single = 'Hello'
double = "World"
multi_line = """This is a
multi-line string.
It preserves line breaks!"""

print(f"  Single quotes: {single}")
print(f"  Double quotes: {double}")
print(f"  Multi-line:\n{multi_line}")


# ----- 2. STRING INDEXING -----
# Each character has a position (index), starting from 0.
print("\n--- 2. String Indexing ---")

word = "PYTHON"
print(f"  word = '{word}'")
print(f"  word[0]  = '{word[0]}'   (first character)")
print(f"  word[3]  = '{word[3]}'   (fourth character)")
print(f"  word[-1] = '{word[-1]}'  (last character)")
print(f"  word[-2] = '{word[-2]}'  (second to last)")


# ----- 3. STRING SLICING -----
# slice = word[start:stop:step]   (stop is NOT included)
print("\n--- 3. String Slicing ---")

text = "Hello, World!"
print(f"  text = '{text}'")
print(f"  text[0:5]   = '{text[0:5]}'")       # Hello
print(f"  text[7:]    = '{text[7:]}'")         # World!
print(f"  text[:5]    = '{text[:5]}'")         # Hello
print(f"  text[::2]   = '{text[::2]}'")        # Every 2nd char
print(f"  text[::-1]  = '{text[::-1]}'")       # Reversed!


# ----- 4. STRING METHODS -----
print("\n--- 4. Essential String Methods ---")

message = "  Python is Amazing  "
print(f"  Original:    '{message}'")
print(f"  .strip()   : '{message.strip()}'")          # Remove whitespace
print(f"  .lower()   : '{message.strip().lower()}'")
print(f"  .upper()   : '{message.strip().upper()}'")
print(f"  .title()   : '{message.strip().title()}'")
print(f"  .replace() : '{message.strip().replace('Amazing', 'Powerful')}'")

email = "user@example.com"
print(f"\n  email = '{email}'")
print(f"  .startswith('user') -> {email.startswith('user')}")
print(f"  .endswith('.com')   -> {email.endswith('.com')}")
print(f"  .find('@')          -> {email.find('@')}  (index of @)")

csv_data = "apple,banana,cherry,mango"
print(f"\n  csv_data = '{csv_data}'")
print(f"  .split(',') -> {csv_data.split(',')}")

fruits_list = ["apple", "banana", "cherry"]
print(f"  ' | '.join(list) -> '{ ' | '.join(fruits_list)}'")


# ----- 5. STRING CHECKING METHODS -----
print("\n--- 5. String Checking Methods ---")

test_values = ["Hello123", "12345", "hello", "   ", "Hello World"]
for val in test_values:
    print(f"  '{val}' -> isalpha:{val.isalpha()}, isdigit:{val.isdigit()}, "
          f"isalnum:{val.isalnum()}, isspace:{val.isspace()}")


# ----- 6. STRING FORMATTING (3 ways) -----
print("\n--- 6. String Formatting ---")

name = "Swati"
age = 25
gpa = 9.87

# Method 1: f-strings (BEST — Python 3.6+)
print(f"  f-string:  Hello, {name}! Age: {age}, GPA: {gpa:.1f}")

# Method 2: .format()
print("  .format(): Hello, {}! Age: {}, GPA: {:.1f}".format(name, age, gpa))

# Method 3: % formatting (old style, but you'll see it in legacy code)
print("  %% style:  Hello, %s! Age: %d, GPA: %.1f" % (name, age, gpa))

# f-string expressions — you can put any Python expression inside {}
print(f"\n  f-string math: 2 ** 10 = {2 ** 10}")
print(f"  f-string call: {'hello world'.title()}")
print(f"  Padding:       |{'left':<15}|{'center':^15}|{'right':>15}|")


# ----- 7. ESCAPE CHARACTERS -----
print("\n--- 7. Escape Characters ---")

print("  Newline:     Line1\\n -> Line1\n                         Line2")
print("  Tab:         Col1\\t -> Col1\tCol2")
print("  Backslash:   \\\\ -> \\")
print("  Quote:       \\\" -> \"inside quotes\"")

# Raw strings ignore escape characters — useful for file paths and regex
path = r"C:\Users\new_folder\test"
print(f"  Raw string:  r'...' -> {path}")


# ----- 8. STRING IMMUTABILITY -----
print("\n--- 8. Strings are IMMUTABLE ---")
print("  You CANNOT change a character in a string directly.")
print("  word = 'Hello'")
print("  word[0] = 'J'  <- This would cause an ERROR!")
print("  Instead: word = 'J' + word[1:]  -> 'Jello'")

demo = "Hello"
demo = "J" + demo[1:]
print(f"  Result: '{demo}'")


# ----- MINI CHALLENGE -----
print("\n" + "=" * 55)
print("  [TROPHY] MINI CHALLENGES")
print("=" * 55)
print("  1. Reverse your name using slicing")
print("  2. Count how many times 'a' appears in 'banana'")
print("  3. Extract the domain from 'user@gmail.com'")
print("  4. Check if 'racecar' is a palindrome using slicing")
print("=" * 55)
