# =============================================================
#  MODULE 09 — FILE HANDLING
#  Level: [WARN] Intermediate
#  Goal:  Read, write, and process files (text, CSV, JSON).
# =============================================================

import os
import csv
import json

print("=" * 55)
print("  MODULE 09 — FILE HANDLING")
print("=" * 55)

# Create a temp directory for our files
os.makedirs("temp_files", exist_ok=True)

# ----- 1. WRITING TEXT FILES -----
print("\n--- 1. Writing a Text File ---")

with open("temp_files/notes.txt", "w") as f:
    f.write("Line 1: Python is powerful.\n")
    f.write("Line 2: File handling is essential.\n")
    f.write("Line 3: Always close your files!\n")

print("  [OK] notes.txt created.")

# ----- 2. READING TEXT FILES -----
print("\n--- 2. Reading a Text File ---")

# Read entire file
with open("temp_files/notes.txt", "r") as f:
    content = f.read()
print(f"  Full content:\n{content}")

# Read line by line
with open("temp_files/notes.txt", "r") as f:
    for i, line in enumerate(f, 1):
        print(f"  Line {i}: {line.strip()}")

# ----- 3. APPENDING -----
print("\n--- 3. Appending to a File ---")

with open("temp_files/notes.txt", "a") as f:
    f.write("Line 4: Appended with mode 'a'.\n")

with open("temp_files/notes.txt", "r") as f:
    print(f"  Updated file has {len(f.readlines())} lines.")

# ----- 4. WORKING WITH CSV -----
print("\n--- 4. CSV Files ---")

# Write CSV
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 22, "A"],
    ["Bob", 25, "B+"],
    ["Charlie", 21, "A-"],
]

with open("temp_files/students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
print("  [OK] students.csv created.")

# Read CSV
with open("temp_files/students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"    {row['Name']}, Age {row['Age']}, Grade {row['Grade']}")

# ----- 5. WORKING WITH JSON -----
print("\n--- 5. JSON Files ---")

config = {
    "app_name": "PyMastery",
    "version": "1.0",
    "features": ["lessons", "quizzes", "projects"],
    "settings": {"theme": "dark", "language": "en"},
}

# Write JSON
with open("temp_files/config.json", "w") as f:
    json.dump(config, f, indent=2)
print("  [OK] config.json created.")

# Read JSON
with open("temp_files/config.json", "r") as f:
    loaded = json.load(f)
print(f"  App: {loaded['app_name']} v{loaded['version']}")
print(f"  Features: {loaded['features']}")

# ----- 6. FILE EXISTENCE & INFO -----
print("\n--- 6. File Info ---")

filepath = "temp_files/notes.txt"
print(f"  Exists:   {os.path.exists(filepath)}")
print(f"  Size:     {os.path.getsize(filepath)} bytes")
print(f"  Is file:  {os.path.isfile(filepath)}")
print(f"  Abs path: {os.path.abspath(filepath)}")

# ----- 7. CONTEXT MANAGERS (why 'with' is important) -----
print("\n--- 7. Why use 'with' statement? ---")
print("  'with' automatically closes the file even if an error occurs.")
print("  Without 'with', you must manually call f.close().")
print("  ALWAYS use 'with' — it's the Pythonic way!")

# ----- CLEANUP (optional) -----
# Uncomment the next 2 lines to clean up temp files:
# import shutil
# shutil.rmtree("temp_files")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a mini diary app (append entries with dates)")
print("  2. Read a CSV, calculate average grade")
print("  3. Create a JSON-based contact book (add/search/delete)")
print("=" * 55)
