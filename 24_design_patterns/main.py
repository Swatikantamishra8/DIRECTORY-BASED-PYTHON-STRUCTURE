# =============================================================
#  MODULE 24 — DESIGN PATTERNS
#  Level: [ERR] Expert
#  Goal:  Implement key Gang-of-Four patterns in Python.
# =============================================================

from abc import ABC, abstractmethod

print("=" * 55)
print("  MODULE 24 — DESIGN PATTERNS")
print("=" * 55)

# ----- 1. SINGLETON -----
print("\n--- 1. Singleton (Only one instance ever) ---")

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connected = False
        return cls._instance

    def connect(self):
        self.connected = True
        return "Connected to DB"

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(f"  db1 is db2: {db1 is db2}")  # True — same instance!
print(f"  {db1.connect()}")

# ----- 2. FACTORY -----
print("\n--- 2. Factory (Create objects without specifying class) ---")

class Notification(ABC):
    @abstractmethod
    def send(self, message): pass

class EmailNotification(Notification):
    def send(self, message):
        return f"[email] Email: {message}"

class SMSNotification(Notification):
    def send(self, message):
        return f"[sms] SMS: {message}"

class PushNotification(Notification):
    def send(self, message):
        return f"[bell] Push: {message}"

class NotificationFactory:
    @staticmethod
    def create(channel):
        channels = {
            "email": EmailNotification,
            "sms": SMSNotification,
            "push": PushNotification,
        }
        cls = channels.get(channel)
        if not cls:
            raise ValueError(f"Unknown channel: {channel}")
        return cls()

for ch in ["email", "sms", "push"]:
    notif = NotificationFactory.create(ch)
    print(f"  {notif.send('Hello!')}")

# ----- 3. OBSERVER -----
print("\n--- 3. Observer (Event system) ---")

class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, data=None):
        for cb in self._listeners.get(event, []):
            cb(data)

emitter = EventEmitter()
emitter.on("user_signup", lambda d: print(f"  [email] Send welcome email to {d}"))
emitter.on("user_signup", lambda d: print(f"  [i] Log signup: {d}"))
emitter.on("user_signup", lambda d: print(f"  [gift] Give bonus to {d}"))

emitter.emit("user_signup", "Swati")

# ----- 4. STRATEGY -----
print("\n--- 4. Strategy (Swap algorithms at runtime) ---")

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, price): pass

class RegularPricing(PricingStrategy):
    def calculate(self, price): return price

class PremiumDiscount(PricingStrategy):
    def calculate(self, price): return price * 0.8

class BlackFridayPricing(PricingStrategy):
    def calculate(self, price): return price * 0.5

class ShoppingCart:
    def __init__(self, strategy: PricingStrategy):
        self.strategy = strategy

    def checkout(self, price):
        return self.strategy.calculate(price)

for name, strat in [("Regular", RegularPricing()),
                     ("Premium", PremiumDiscount()),
                     ("BlackFriday", BlackFridayPricing())]:
    cart = ShoppingCart(strat)
    print(f"  {name:<12} $100 -> ${cart.checkout(100):.0f}")

# ----- 5. DECORATOR PATTERN -----
print("\n--- 5. Decorator Pattern (Wrap behavior) ---")

class Coffee:
    def cost(self): return 5.0
    def description(self): return "Plain Coffee"

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self): return self._coffee.cost() + 1.5
    def description(self): return self._coffee.description() + " + Milk"

class SugarDecorator:
    def __init__(self, coffee):
        self._coffee = coffee
    def cost(self): return self._coffee.cost() + 0.5
    def description(self): return self._coffee.description() + " + Sugar"

order = SugarDecorator(MilkDecorator(Coffee()))
print(f"  {order.description()} = ${order.cost():.2f}")

# ----- 6. REPOSITORY PATTERN -----
print("\n--- 6. Repository (Data access abstraction) ---")

class UserRepository:
    def __init__(self):
        self._users = {}
        self._next_id = 1

    def create(self, name, email):
        user = {"id": self._next_id, "name": name, "email": email}
        self._users[self._next_id] = user
        self._next_id += 1
        return user

    def find_by_id(self, user_id):
        return self._users.get(user_id)

    def find_all(self):
        return list(self._users.values())

repo = UserRepository()
repo.create("Alice", "alice@test.com")
repo.create("Bob", "bob@test.com")
print(f"  All users: {repo.find_all()}")
print(f"  User 1:    {repo.find_by_id(1)}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Implement a Command pattern (undo/redo)")
print("  2. Build a plugin system with Observer pattern")
print("  3. Create a middleware chain (Chain of Responsibility)")
print("=" * 55)
