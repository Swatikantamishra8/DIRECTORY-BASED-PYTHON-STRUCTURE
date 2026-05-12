# =============================================================
#  MODULE 14 — DECORATORS & GENERATORS
#  Level: 🟠 Advanced
#  Goal:  Master decorators, closures, generators, itertools.
# =============================================================

import time
import functools
import itertools

print("=" * 55)
print("  MODULE 14 — DECORATORS & GENERATORS")
print("=" * 55)

# ===================== DECORATORS =====================
print("\n" + "=" * 55)
print("  PART 1: DECORATORS")
print("=" * 55)

# ----- 1. CLOSURES (Foundation for decorators) -----
print("\n--- 1. Closures ---")

def multiplier(factor):
    def inner(number):
        return number * factor
    return inner

double = multiplier(2)
triple = multiplier(3)
print(f"  double(5) = {double(5)}")
print(f"  triple(5) = {triple(5)}")

# ----- 2. BASIC DECORATOR -----
print("\n--- 2. Basic Decorator ---")

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"    [log] Calling {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"    [OK] {func.__name__} returned: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)

# ----- 3. TIMER DECORATOR -----
print("\n--- 3. Timer Decorator ---")

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"    [time]  {func.__name__} took {elapsed:.6f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)

# ----- 4. DECORATOR WITH ARGUMENTS -----
print("\n--- 4. Decorator with Arguments ---")

def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hello(name):
    print(f"    Hello, {name}!")

say_hello("Swati")

# ----- 5. STACKING DECORATORS -----
print("\n--- 5. Stacking Decorators ---")

@timer
@logger
def multiply(a, b):
    return a * b

multiply(6, 7)


# ===================== GENERATORS =====================
print("\n" + "=" * 55)
print("  PART 2: GENERATORS")
print("=" * 55)

# ----- 6. BASIC GENERATOR -----
print("\n--- 6. Basic Generator (yield) ---")

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("  Countdown:", list(countdown(5)))

# Generators are LAZY — they compute one value at a time
gen = countdown(3)
print(f"  next() = {next(gen)}")
print(f"  next() = {next(gen)}")
print(f"  next() = {next(gen)}")

# ----- 7. GENERATOR EXPRESSION -----
print("\n--- 7. Generator Expression ---")

# List comprehension -> creates entire list in memory
squares_list = [x**2 for x in range(10)]

# Generator expression -> creates values on demand (memory efficient!)
squares_gen = (x**2 for x in range(10))

print(f"  List:      {squares_list}")
print(f"  Generator: {squares_gen}")
print(f"  Sum of gen: {sum(x**2 for x in range(10))}")

# ----- 8. INFINITE GENERATOR -----
print("\n--- 8. Infinite Generator ---")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(f"  First 10 Fibonacci: {first_10}")

# ----- 9. ITERTOOLS (Preview) -----
print("\n--- 9. itertools ---")

print(f"  count(10):    {list(itertools.islice(itertools.count(10), 5))}")
print(f"  cycle('AB'):  {list(itertools.islice(itertools.cycle('AB'), 6))}")
print(f"  chain([1],[2]): {list(itertools.chain([1,2], [3,4], [5]))}")
print(f"  combinations: {list(itertools.combinations('ABC', 2))}")
print(f"  permutations: {list(itertools.permutations('AB', 2))}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Create a @cache decorator (memoization)")
print("  2. Build a @retry(max=3) decorator")
print("  3. Write a generator that yields prime numbers")
print("=" * 55)
