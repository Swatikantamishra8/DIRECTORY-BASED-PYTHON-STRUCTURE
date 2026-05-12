# =============================================================
#  MODULE 15 — FUNCTIONAL PROGRAMMING
#  Level: 🟠 Advanced
#  Goal:  Pure functions, map/filter/reduce, partial, compose.
# =============================================================

from functools import reduce, partial

print("=" * 55)
print("  MODULE 15 — FUNCTIONAL PROGRAMMING")
print("=" * 55)

# ----- 1. PURE FUNCTIONS -----
print("\n--- 1. Pure Functions ---")
print("  A pure function: same input -> always same output, no side effects.")

def pure_add(a, b):
    return a + b  # No mutation, no print, just a return

print(f"  pure_add(3, 4) = {pure_add(3, 4)}")

# ----- 2. MAP -----
print("\n--- 2. map() — Transform every item ---")

names = ["alice", "bob", "charlie"]
capitalized = list(map(str.title, names))
print(f"  Titles: {capitalized}")

prices = [10.5, 23.0, 7.99, 45.0]
with_tax = list(map(lambda p: round(p * 1.18, 2), prices))
print(f"  With 18% tax: {with_tax}")

# ----- 3. FILTER -----
print("\n--- 3. filter() — Keep only matching items ---")

numbers = list(range(1, 21))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"  Evens from 1-20: {evens}")

words = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, words))  # Removes falsy values
print(f"  Non-empty: {non_empty}")

# ----- 4. REDUCE -----
print("\n--- 4. reduce() — Accumulate to single value ---")

nums = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, nums)
product = reduce(lambda acc, x: acc * x, nums)
maximum = reduce(lambda a, b: a if a > b else b, nums)

print(f"  Sum of {nums}     = {total}")
print(f"  Product of {nums} = {product}")
print(f"  Max of {nums}     = {maximum}")

# ----- 5. PARTIAL FUNCTIONS -----
print("\n--- 5. partial() — Pre-fill arguments ---")

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"  square(5) = {square(5)}")
print(f"  cube(5)   = {cube(5)}")

# ----- 6. FUNCTION COMPOSITION -----
print("\n--- 6. Function Composition ---")

def compose(*funcs):
    """Compose functions right-to-left: compose(f, g)(x) = f(g(x))."""
    return reduce(lambda f, g: lambda x: f(g(x)), funcs)

double = lambda x: x * 2
increment = lambda x: x + 1
square_fn = lambda x: x ** 2

transform = compose(square_fn, increment, double)
print(f"  compose(square, +1, double)(3) = {transform(3)}")
print(f"  Step: 3 -> double(3)=6 -> +1=7 -> square=49")

# ----- 7. ALL, ANY, SORTED with key -----
print("\n--- 7. all(), any(), sorted() ---")

scores = [85, 92, 78, 95, 88]
print(f"  All above 70? {all(s > 70 for s in scores)}")
print(f"  Any above 90? {any(s > 90 for s in scores)}")

students = [
    {"name": "Alice", "gpa": 3.9},
    {"name": "Bob", "gpa": 3.5},
    {"name": "Charlie", "gpa": 3.8},
]
by_gpa = sorted(students, key=lambda s: s["gpa"], reverse=True)
for s in by_gpa:
    print(f"    {s['name']}: {s['gpa']}")

# ----- 8. CHAINING OPERATIONS (Pipeline style) -----
print("\n--- 8. Pipeline Pattern ---")

data = range(1, 101)

result = (
    reduce(lambda acc, x: acc + x,
        filter(lambda x: x > 20,
            map(lambda x: x ** 2,
                filter(lambda x: x % 2 == 0, data)
            )
        )
    )
)
print(f"  Pipeline: even 1-100 -> square -> keep >20 -> sum = {result}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a data processing pipeline with compose()")
print("  2. Implement your own map/filter using reduce")
print("  3. Create a partial-based unit converter library")
print("=" * 55)
