# =============================================================
#  MODULE 18 — DATABASE WITH PYTHON (SQLite)
#  Level: 🟠 Advanced
#  Goal:  CRUD operations, SQL basics, ORM-like patterns.
# =============================================================

import sqlite3
import os

print("=" * 55)
print("  MODULE 18 — DATABASE WITH PYTHON")
print("=" * 55)

DB_PATH = "temp_files/school.db"
os.makedirs("temp_files", exist_ok=True)

# Remove old DB for clean run
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# ----- 1. CONNECT & CREATE TABLE -----
print("\n--- 1. Create Database & Table ---")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT,
        gpa REAL
    )
""")
conn.commit()
print("  [OK] Table 'students' created.")

# ----- 2. INSERT (Create) -----
print("\n--- 2. INSERT — Adding Records ---")

students = [
    ("Alice", 22, "A", 3.9),
    ("Bob", 25, "B+", 3.5),
    ("Charlie", 21, "A-", 3.8),
    ("Diana", 23, "A+", 4.0),
    ("Eve", 24, "B", 3.2),
]

cursor.executemany(
    "INSERT INTO students (name, age, grade, gpa) VALUES (?, ?, ?, ?)",
    students,
)
conn.commit()
print(f"  [OK] Inserted {len(students)} students.")

# ----- 3. SELECT (Read) -----
print("\n--- 3. SELECT — Reading Records ---")

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(f"  {'ID':<4} {'Name':<10} {'Age':<5} {'Grade':<6} {'GPA':<5}")
print(f"  {'-'*30}")
for row in rows:
    print(f"  {row[0]:<4} {row[1]:<10} {row[2]:<5} {row[3]:<6} {row[4]:<5}")

# WHERE clause
print("\n  Students with GPA >= 3.8:")
cursor.execute("SELECT name, gpa FROM students WHERE gpa >= ?", (3.8,))
for name, gpa in cursor.fetchall():
    print(f"    [*] {name}: {gpa}")

# ----- 4. UPDATE -----
print("\n--- 4. UPDATE — Modifying Records ---")

cursor.execute("UPDATE students SET gpa = ? WHERE name = ?", (3.6, "Bob"))
conn.commit()

cursor.execute("SELECT name, gpa FROM students WHERE name = 'Bob'")
print(f"  Bob's updated GPA: {cursor.fetchone()[1]}")

# ----- 5. DELETE -----
print("\n--- 5. DELETE — Removing Records ---")

cursor.execute("DELETE FROM students WHERE name = ?", ("Eve",))
conn.commit()

cursor.execute("SELECT COUNT(*) FROM students")
print(f"  Students remaining: {cursor.fetchone()[0]}")

# ----- 6. AGGREGATE QUERIES -----
print("\n--- 6. Aggregate Queries ---")

cursor.execute("SELECT AVG(gpa), MAX(gpa), MIN(gpa) FROM students")
avg, mx, mn = cursor.fetchone()
print(f"  Average GPA: {avg:.2f}")
print(f"  Highest GPA: {mx}")
print(f"  Lowest GPA:  {mn}")

cursor.execute("SELECT grade, COUNT(*) FROM students GROUP BY grade")
print("\n  Grade Distribution:")
for grade, count in cursor.fetchall():
    print(f"    {grade}: {count} student(s)")

# ----- 7. ROW FACTORY (dict-like access) -----
print("\n--- 7. Row Factory ---")

conn.row_factory = sqlite3.Row
cursor = conn.cursor()
cursor.execute("SELECT * FROM students LIMIT 2")
for row in cursor.fetchall():
    print(f"  {dict(row)}")

# ----- 8. CONTEXT MANAGER PATTERN -----
print("\n--- 8. Best Practice: Context Manager ---")
print("  Always use 'with' to auto-commit/rollback:")
print("    with sqlite3.connect('db.sqlite') as conn:")
print("        conn.execute('INSERT ...')")
print("  Commits on success, rolls back on error.")

# Cleanup
conn.close()
print(f"\n  [OK] Database saved to {DB_PATH}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Build a CLI contact book backed by SQLite")
print("  2. Create an inventory management system")
print("  3. Build a quiz app that stores scores in a DB")
print("=" * 55)
