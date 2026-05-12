# =============================================================
#  MODULE 16 — REGULAR EXPRESSIONS
#  Level: 🟠 Advanced
#  Goal:  Pattern matching, extraction, and substitution.
# =============================================================

import re

print("=" * 55)
print("  MODULE 16 — REGULAR EXPRESSIONS")
print("=" * 55)

# ----- 1. BASIC MATCHING -----
print("\n--- 1. Basic Matching ---")

text = "Hello, my email is dev@example.com and I was born in 1998."

# re.search() — find first match
match = re.search(r"\d+", text)
print(f"  First number found: {match.group()}")

# re.findall() — find ALL matches
all_numbers = re.findall(r"\d+", text)
print(f"  All numbers: {all_numbers}")

# ----- 2. COMMON PATTERNS -----
print("\n--- 2. Common Patterns ---")

patterns = {
    r"\d":     "Digit (0-9)",
    r"\D":     "Non-digit",
    r"\w":     "Word char (a-z, A-Z, 0-9, _)",
    r"\s":     "Whitespace",
    r".":      "Any character except newline",
    r"\b":     "Word boundary",
}
for pat, desc in patterns.items():
    print(f"    {pat:<8} -> {desc}")

print("\n  Quantifiers:")
quantifiers = {
    "*":    "0 or more",
    "+":    "1 or more",
    "?":    "0 or 1",
    "{3}":  "Exactly 3",
    "{2,5}": "Between 2 and 5",
}
for q, desc in quantifiers.items():
    print(f"    {q:<8} -> {desc}")

# ----- 3. EMAIL VALIDATION -----
print("\n--- 3. Email Validation ---")

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = ["user@gmail.com", "bad@", "hello@world.co.in", "no-at-sign"]
for email in emails:
    valid = "[OK]" if re.match(email_pattern, email) else "[X]"
    print(f"    {valid} {email}")

# ----- 4. GROUPS AND CAPTURE -----
print("\n--- 4. Groups ---")

date_text = "Today is 2026-05-13 and tomorrow is 2026-05-14."
date_pattern = r"(\d{4})-(\d{2})-(\d{2})"

for match in re.finditer(date_pattern, date_text):
    year, month, day = match.groups()
    print(f"    Date: {day}/{month}/{year}")

# Named groups
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
m = re.search(pattern, date_text)
print(f"    Named: {m.group('day')}/{m.group('month')}/{m.group('year')}")

# ----- 5. SUBSTITUTION -----
print("\n--- 5. re.sub() — Find and Replace ---")

messy = "Hello    World,   this    has    extra   spaces."
clean = re.sub(r"\s+", " ", messy)
print(f"    Before: '{messy}'")
print(f"    After:  '{clean}'")

# Censor phone numbers
text2 = "Call me at 9876543210 or 8765432109."
censored = re.sub(r"\d{10}", "XXX-XXX-XXXX", text2)
print(f"    Censored: {censored}")

# ----- 6. SPLIT -----
print("\n--- 6. re.split() ---")

sentence = "Hello;World,Python:Rocks"
parts = re.split(r"[;,:]", sentence)
print(f"    Split on ;,: -> {parts}")

# ----- 7. FLAGS -----
print("\n--- 7. Flags ---")

text3 = "Python is GREAT\npython is fun"
matches = re.findall(r"python", text3, re.IGNORECASE)
print(f"    Case-insensitive: {matches}")

# ----- 8. REAL-WORLD: Log Parser -----
print("\n--- 8. Real-World: Log Parser ---")

logs = [
    "2026-05-13 10:30:15 ERROR Database connection failed",
    "2026-05-13 10:30:16 INFO  Server restarted",
    "2026-05-13 10:30:17 WARN  Memory usage at 85%",
    "2026-05-13 10:30:18 ERROR Timeout on API call",
]

log_pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+)\s+(.*)"
for log in logs:
    m = re.match(log_pattern, log)
    if m:
        date, time_val, level, msg = m.groups()
        icon = "[ERR]" if level == "ERROR" else "[WARN]" if level == "WARN" else "[OK]"
        print(f"    {icon} [{time_val}] {msg}")

print("\n" + "=" * 55)
print("  [TROPHY] CHALLENGES")
print("=" * 55)
print("  1. Extract all URLs from a paragraph of text")
print("  2. Validate Indian phone numbers (+91 format)")
print("  3. Build a Markdown bold/italic parser with re.sub()")
print("=" * 55)
