rint("--- Step 2: Basic Math & Operations ---")

# In our last lesson, we used input() to get the user's age.
# However, input() ALWAYS returns text (called a "string"), even if you type a number!
age_text = input("How old are you? ")

# To do math, we must convert that text into a whole number (called an "integer").
# We use the int() function for this:
age = int(age_text)

print("\n--- Let's do some math! ---")

# 1. Subtraction (-)
# The current year is roughly 2026 (based on my system clock)
birth_year = 2026 - age 
print(f"If you are {age} years old in 2026, you were probably born around {birth_year}.")

# 2. Multiplication (*)
# Let's calculate roughly how many days you've been alive
days_alive = age * 365
print(f"Wow! You have been alive for roughly {days_alive} days!")

# 3. Division (/)
# Let's see how many decades you've lived
decades = age / 10
print(f"You have lived for {decades} decades.")

# 4. Modulo (%) 
# This is a special math operator. It gives you the REMAINDER of a division.
remainder = age % 10
print(f"Or in other words, you are {int(age/10)} full decades and {remainder} years old!")
