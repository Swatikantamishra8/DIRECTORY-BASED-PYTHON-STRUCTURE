# =============================================================
#  MODULE 13 — OOP ADVANCED
#  Level: 🟠 Advanced
#  Goal:  Inheritance, Polymorphism, ABCs, MRO, Dataclasses.
# =============================================================

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

print("=" * 55)
print("  MODULE 13 — OOP ADVANCED")
print("=" * 55)

# ----- 1. INHERITANCE -----
print("\n--- 1. Inheritance ---")

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")
        self.breed = breed

    def fetch(self):
        return f"{self.name} fetches the ball! (ball)"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow")

    def purr(self):
        return f"{self.name} purrs... (cat)"

dog = Dog("Buddy", "Lab")
cat = Cat("Whiskers")
print(f"  {dog.speak()}")
print(f"  {dog.fetch()}")
print(f"  {cat.speak()}")
print(f"  {cat.purr()}")

# ----- 2. POLYMORPHISM -----
print("\n--- 2. Polymorphism ---")

animals = [Dog("Rex", "Husky"), Cat("Luna"), Animal("Parrot", "Squawk")]
for animal in animals:
    print(f"  {animal.speak()}")

# ----- 3. ABSTRACT BASE CLASSES -----
print("\n--- 3. Abstract Base Classes (ABCs) ---")

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(f"  {s.describe()}, perimeter={s.perimeter():.2f}")

# ----- 4. MULTIPLE INHERITANCE & MRO -----
print("\n--- 4. Multiple Inheritance & MRO ---")

class Flyable:
    def fly(self):
        return "I can fly! (fly)"

class Swimmable:
    def swim(self):
        return "I can swim! (swim)"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Quack")

donald = Duck("Donald")
print(f"  {donald.speak()}")
print(f"  {donald.fly()}")
print(f"  {donald.swim()}")
print(f"  MRO: {[c.__name__ for c in Duck.__mro__]}")

# ----- 5. DATACLASSES -----
print("\n--- 5. Dataclasses (Python 3.7+) ---")

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    @property
    def total_value(self):
        return self.price * self.quantity

p1 = Product("Laptop", 999.99, 5)
p2 = Product("Mouse", 29.99, 50)
print(f"  {p1}")
print(f"  {p2}")
print(f"  {p1.name} total value: ${p1.total_value:.2f}")
print(f"  p1 == p2: {p1 == p2}")

# ----- 6. COMPOSITION OVER INHERITANCE -----
print("\n--- 6. Composition vs Inheritance ---")

class Engine:
    def __init__(self, horsepower):
        self.hp = horsepower
    def start(self):
        return f"Engine ({self.hp}hp) started (!)"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition: Car HAS-A Engine

    def drive(self):
        return f"{self.brand}: {self.engine.start()} -> Driving!"

car = Car("Tesla", Engine(670))
print(f"  {car.drive()}")
print("  [TIP] Prefer composition when 'HAS-A' makes more sense than 'IS-A'")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a shape hierarchy with Triangle, Square")
print("  2. Create an Employee system (Manager, Developer)")
print("  3. Implement a Plugin system using ABCs")
print("=" * 55)
