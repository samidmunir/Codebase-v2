# Harvard CS50's Intro Python Programming Course
# freeCodeCamp.org
# September 9th, 2024
# variables
#   main.py

# ask a user for their name.
name = input("What's your name?\n--> ")

# say hello to the user.
print("\nHello,", name, sep = ' ', end = '\n')

# say hello to user using format_string.
# - using split() to remove any whitespace on left/right.
name = name.strip()
# name = name.capitalize()
name = name.title()
# we can also chain these functions right after one another for cleaner code.
# name = input("What's your name?\n--> ").strip().title()
print(f"\nHello, {name}")

# splitting the user's name into first/last name
first_name, last_name = name.split(" ")
print(f"\nFirst name: {first_name}\nLast name: {last_name}")
print(f"--> {first_name} {last_name[0]}.")

# integers in Python
a = 2
b = 3
sum = a + b
print(f"\na: {a} and b: {b}")
print(f"a + b = {sum}")

a = 999
b = 1
sum = a + b
print(f"\na: {a} and b: {b}")
print(f"a + b = {sum:,}")

a = 2
b = 3
q = a / b
print(f"\na: {a} and b: {b}")
print(f"a / b = {round(q, 2)}")

a = 3
b = 14
q = a / b
print(f"\na: {a} and b: {b}")
print(f"a / b = {q:.2f}")