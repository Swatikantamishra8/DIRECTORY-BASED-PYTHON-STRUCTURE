 We are going to ask the user a few questions and store their answers in variables.

print("--- Let's get to know you! ---")

# The input() function pauses the program and waits for the user to type something.
# We then save what they typed into variables like 'name', 'age', etc.
name = input("What is your name? ")
age = input("How old are you? ")
interest = input("What are your hobbies or interests? ")
aim = input("What is your main aim in learning Python? ")

# The '\n' creates a blank new line to make the output look clean.
print("\n--- Your Personalized Profile ---")

# Using f-strings (putting an 'f' before the quotes) lets us inject our variables directly into the text using {}
print(f"Hello {name}! It is wonderful to meet you.")
print(f"Being {age} years old brings great life experience, making it the perfect time to pursue your aim to {aim}.")
print(f"And when you need a break from studying Python, you can always relax and enjoy {interest}!")
print("Let's make this coding journey an amazing one!")
