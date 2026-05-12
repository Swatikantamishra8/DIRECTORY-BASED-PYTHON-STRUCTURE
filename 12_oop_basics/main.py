# =============================================================
#  MODULE 12 — OOP BASICS
#  Level: [WARN] Intermediate
#  Goal:  Understand classes, objects, __init__, methods,
#         class vs instance variables, and encapsulation.
# =============================================================

print("=" * 55)
print("  MODULE 12 — OOP BASICS")
print("=" * 55)

# ----- 1. YOUR FIRST CLASS -----
print("\n--- 1. First Class ---")

class Dog:
    """A simple Dog class."""

    # Class variable (shared by ALL dogs)
    species = "Canis familiaris"

    def __init__(self, name, breed, age):
        # Instance variables (unique to each dog)
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof! (dog)"

    def info(self):
        return f"{self.name} | {self.breed} | {self.age} years"

# Creating objects (instances)
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Max", "German Shepherd", 5)

print(f"  {dog1.info()}")
print(f"  {dog2.info()}")
print(f"  {dog1.bark()}")
print(f"  Species: {Dog.species}")

# ----- 2. CLASS vs INSTANCE VARIABLES -----
print("\n--- 2. Class vs Instance Variables ---")

class Counter:
    total = 0  # Class variable

    def __init__(self, name):
        self.name = name     # Instance variable
        self.count = 0       # Instance variable
        Counter.total += 1

    def increment(self):
        self.count += 1

c1 = Counter("Page Views")
c2 = Counter("Clicks")
c1.increment()
c1.increment()
c2.increment()

print(f"  {c1.name}: {c1.count}")
print(f"  {c2.name}: {c2.count}")
print(f"  Total Counter objects created: {Counter.total}")

# ----- 3. METHODS: instance, class, static -----
print("\n--- 3. Method Types ---")

class MathHelper:
    pi = 3.14159

    def __init__(self, value):
        self.value = value

    # Instance method — uses self
    def square(self):
        return self.value ** 2

    # Class method — uses cls (the class itself)
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    # Static method — no self or cls (just a utility)
    @staticmethod
    def add(a, b):
        return a + b

m = MathHelper(7)
print(f"  Instance: 7^2 = {m.square()}")
print(f"  Class:    circle area(5) = {MathHelper.circle_area(5):.2f}")
print(f"  Static:   add(3, 4) = {MathHelper.add(3, 4)}")

# ----- 4. ENCAPSULATION -----
print("\n--- 4. Encapsulation (Public / Private) ---")

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner          # Public
        self.__balance = balance    # Private (name mangling)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited Rs.{amount}"
        return "Invalid amount"

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account({self.owner}, Rs.{self.__balance})"

acc = BankAccount("Swati", 1000)
acc.deposit(500)
print(f"  {acc}")
print(f"  Balance via getter: Rs.{acc.get_balance()}")
# print(acc.__balance)  <- Would raise AttributeError!

# ----- 5. PROPERTY DECORATOR -----
print("\n--- 5. @property (Pythonic getters/setters) ---")

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

temp = Temperature(100)
print(f"  {temp.celsius}°C = {temp.fahrenheit}°F")

temp.celsius = 0
print(f"  {temp.celsius}°C = {temp.fahrenheit}°F")

# ----- 6. DUNDER METHODS -----
print("\n--- 6. Dunder (Magic) Methods ---")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(f"  v1 = {v1}")
print(f"  v2 = {v2}")
print(f"  v1 + v2 = {v1 + v2}")
print(f"  v1 == v2 = {v1 == v2}")
print(f"  len(v1)  = {len(v1)}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Create a Library system (Book, Library classes)")
print("  2. Build a Student grade tracker with @property")
print("  3. Create a Playlist class with dunder methods")
print("=" * 55)
