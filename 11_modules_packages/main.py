# =============================================================
#  MODULE 11 — MODULES & PACKAGES
#  Level: [WARN] Intermediate
#  Goal:  Organize code into modules, use pip, create packages.
# =============================================================

import math
import random
import datetime
import os
import sys

print("=" * 55)
print("  MODULE 11 — MODULES & PACKAGES")
print("=" * 55)

# ----- 1. BUILT-IN MODULES -----
print("\n--- 1. Built-in Modules ---")

# math module
print(f"  math.pi      = {math.pi}")
print(f"  math.sqrt(64) = {math.sqrt(64)}")
print(f"  math.ceil(4.2) = {math.ceil(4.2)}")
print(f"  math.floor(4.8) = {math.floor(4.8)}")

# random module
print(f"\n  random.randint(1,100) = {random.randint(1, 100)}")
print(f"  random.choice(['a','b','c']) = {random.choice(['a','b','c'])}")

colors = ["red", "blue", "green", "yellow"]
random.shuffle(colors)
print(f"  random.shuffle(colors) = {colors}")

# datetime module
now = datetime.datetime.now()
print(f"\n  Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Year: {now.year}, Month: {now.month}, Day: {now.day}")

# os module
print(f"\n  OS name:     {os.name}")
print(f"  Current dir: {os.getcwd()}")

# sys module
print(f"  Python ver:  {sys.version.split()[0]}")

# ----- 2. IMPORT STYLES -----
print("\n--- 2. Import Styles ---")
print("  import math            -> math.sqrt(4)")
print("  from math import sqrt  -> sqrt(4)")
print("  from math import *     -> sqrt(4)  [NOT recommended]")
print("  import math as m       -> m.sqrt(4)")

# ----- 3. CREATING YOUR OWN MODULE -----
print("\n--- 3. Custom Module (concept) ---")
print("  1. Create a file: helpers.py")
print("  2. Define functions inside it")
print("  3. In main.py: from helpers import my_function")
print("  4. That's it! Your code is now reusable.")

# ----- 4. __name__ == '__main__' -----
print("\n--- 4. The __name__ guard ---")
print(f"  Current __name__ = '{__name__}'")
print("  When a file is RUN directly: __name__ = '__main__'")
print("  When a file is IMPORTED:     __name__ = 'module_name'")

if __name__ == "__main__":
    print("  [OK] This file is being run directly!")

# ----- 5. PIP & VIRTUAL ENVIRONMENTS -----
print("\n--- 5. pip & venv (Commands) ---")
print("  pip install requests        -> Install a package")
print("  pip list                    -> See installed packages")
print("  pip freeze > requirements.txt -> Save dependencies")
print("  python -m venv myenv        -> Create virtual env")
print("  myenv\\Scripts\\activate      -> Activate (Windows)")
print("  pip install -r requirements.txt -> Install all deps")

# ----- 6. POPULAR THIRD-PARTY PACKAGES -----
print("\n--- 6. Popular Packages ---")
packages = {
    "requests":    "HTTP requests (APIs)",
    "flask":       "Web framework (lightweight)",
    "django":      "Web framework (full-featured)",
    "pandas":      "Data analysis",
    "numpy":       "Numerical computing",
    "pytest":      "Testing framework",
    "black":       "Code formatter",
    "sqlalchemy":  "Database ORM",
}
for pkg, desc in packages.items():
    print(f"    {pkg:<14} -> {desc}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Create a helpers.py with 5 utility functions, import them")
print("  2. Build a random quote generator using random module")
print("  3. Create a package with __init__.py (folder as module)")
print("=" * 55)
