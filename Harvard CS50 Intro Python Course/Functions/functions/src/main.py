# Harvard CS50's Intro Python Programming Course
# freeCodeCamp.org
# September 9th, 2024
# functions
#   main.py

def say_hello(name = "john doe"):
    print("\nrunning function say_hello() -->")
    f_name, l_name = name.split()
    print(f"\tHello, {f_name.capitalize()} {l_name.capitalize()[0]}.")

def main():
    name = input("What's your full name?\n")
    say_hello(name)

main()
