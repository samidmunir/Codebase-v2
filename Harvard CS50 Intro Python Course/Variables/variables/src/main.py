# Harvard CS50's Intro Python Programming Course
# freeCodeCamp.org
# September 9th, 2024
# variables
#   main.py

# ask a user for their name.
name = input("What's your name?\n--> ")

# say hello to the user.
print("\nHello,", name, sep = ' ', end = '\n')

# say hello to user using format_string
# - using split() to remove any whitespace on left/right
name = name.strip()
print(f"\nHello, {name}")