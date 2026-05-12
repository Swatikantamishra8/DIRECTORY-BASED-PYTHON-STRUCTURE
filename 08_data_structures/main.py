# =============================================================
#  MODULE 08 — DATA STRUCTURES
#  Level: [WARN] Intermediate
#  Goal:  Master Lists, Tuples, Dictionaries, Sets,
#         and Comprehensions.
# =============================================================

print("=" * 55)
print("  MODULE 08 — DATA STRUCTURES")
print("=" * 55)

# ===================== LISTS =====================
print("\n" + "=" * 55)
print("  PART 1: LISTS (Ordered, Mutable)")
print("=" * 55)

fruits = ["apple", "banana", "cherry", "mango"]
print(f"  Original:   {fruits}")

# Accessing
print(f"  First:      {fruits[0]}")
print(f"  Last:       {fruits[-1]}")
print(f"  Slice[1:3]: {fruits[1:3]}")

# Modifying
fruits.append("grape")
print(f"  After append('grape'): {fruits}")

fruits.insert(1, "kiwi")
print(f"  After insert(1,'kiwi'): {fruits}")

fruits.remove("banana")
print(f"  After remove('banana'): {fruits}")

popped = fruits.pop()
print(f"  After pop(): {fruits}, popped='{popped}'")

# Sorting
numbers = [34, 12, 89, 56, 7]
numbers.sort()
print(f"  Sorted:   {numbers}")
numbers.sort(reverse=True)
print(f"  Reversed: {numbers}")

# List Comprehension
squares = [x**2 for x in range(1, 11)]
print(f"  Squares 1-10: {squares}")

evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"  Evens 1-20:   {evens}")


# ===================== TUPLES =====================
print("\n" + "=" * 55)
print("  PART 2: TUPLES (Ordered, Immutable)")
print("=" * 55)

coordinates = (10.5, 20.3)
print(f"  Coordinates: {coordinates}")
print(f"  X: {coordinates[0]}, Y: {coordinates[1]}")

# Unpacking
name, age, city = ("Swati", 25, "India")
print(f"  Unpacked: name={name}, age={age}, city={city}")

# Tuple as dict key (lists can't do this!)
locations = {(28.6, 77.2): "Delhi", (19.0, 72.8): "Mumbai"}
print(f"  Location at (28.6, 77.2): {locations[(28.6, 77.2)]}")

# Named tuples (preview)
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 7)
print(f"  Named tuple: {p}, x={p.x}, y={p.y}")


# ===================== DICTIONARIES =====================
print("\n" + "=" * 55)
print("  PART 3: DICTIONARIES (Key-Value, Mutable)")
print("=" * 55)

student = {
    "name": "Swati",
    "age": 25,
    "skills": ["Python", "SQL", "Git"],
    "is_active": True,
}
print(f"  Student: {student}")
print(f"  Name:    {student['name']}")
print(f"  Skills:  {student['skills']}")

# Safe access with .get()
print(f"  GPA:     {student.get('gpa', 'Not set')}")

# Adding / Updating
student["gpa"] = 9.2
student["age"] = 26
print(f"  Updated: {student}")

# Looping
print("\n  Iterating:")
for key, value in student.items():
    print(f"    {key:>10}: {value}")

# Dict comprehension
word = "abracadabra"
freq = {char: word.count(char) for char in set(word)}
print(f"\n  Frequency of '{word}': {freq}")

# Nested dictionary
company = {
    "engineering": {"lead": "Alice", "size": 15},
    "design":      {"lead": "Bob",   "size": 8},
}
print(f"  Eng lead: {company['engineering']['lead']}")


# ===================== SETS =====================
print("\n" + "=" * 55)
print("  PART 4: SETS (Unordered, Unique)")
print("=" * 55)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"  A: {set_a}")
print(f"  B: {set_b}")
print(f"  Union       A|B:  {set_a | set_b}")
print(f"  Intersection A&B: {set_a & set_b}")
print(f"  Difference  A-B:  {set_a - set_b}")
print(f"  Symmetric   A^B:  {set_a ^ set_b}")

# Remove duplicates from a list
dupes = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(dupes))
print(f"  Deduplicated: {dupes} -> {unique}")

# Set comprehension
even_set = {x for x in range(20) if x % 2 == 0}
print(f"  Even set: {even_set}")


# ===================== CHOOSING THE RIGHT STRUCTURE =====================
print("\n" + "=" * 55)
print("  WHEN TO USE WHAT?")
print("=" * 55)
print("  List  -> Ordered collection, allows duplicates")
print("  Tuple -> Immutable list, good for fixed data / dict keys")
print("  Dict  -> Key-value lookups, fast access by key")
print("  Set   -> Unique items, set math (union, intersection)")

# ----- MINI CHALLENGE -----
print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Count word frequency in a paragraph (dict)")
print("  2. Find common friends between two users (sets)")
print("  3. Build a contact book using nested dicts")
print("=" * 55)
