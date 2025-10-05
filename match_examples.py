# ================================
# Python Match Statement
# Full Tutorial with Examples
# ================================

# Match statement is available from Python 3.10+
# It is similar to switch-case in other programming languages.

# Example 1: Simple Match
value = 2

match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")  # This will print
    case 3:
        print("Value is 3")
    case _:
        print("Value is something else")  # Default case

# ----------------------------------------------------

# Example 2: Match with multiple options in one case
fruit = "apple"

match fruit:
    case "apple" | "banana" | "orange":
        print("This is a common fruit")
    case "mango":
        print("This is a tropical fruit")
    case _:
        print("Unknown fruit")

# ----------------------------------------------------

# Example 3: Match with pattern matching (tuple)
point = (0, 1)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y} on Y-axis")  # Matches any point with x=0
    case (x, 0):
        print(f"X={x} on X-axis")  # Matches any point with y=0
    case (x, y):
        print(f"Point at ({x}, {y})")  # Default match

# ----------------------------------------------------

# Example 4: Match with dictionary pattern
person = {"name": "Alice", "age": 25}

match person:
    case {"name": "Alice", "age": age}:
        print(f"Alice is {age} years old")
    case {"name": name}:
        print(f"Hello {name}")
    case _:
        print("Unknown person")

# ----------------------------------------------------

# Example 5: Match with guards
number = 15

match number:
    case n if n % 2 == 0:
        print("Even number")
    case n if n % 2 != 0:
        print("Odd number")

# ----------------------------------------------------

# Example 6: User input with match
day = input("Enter a day (e.g., Monday): ")

match day.capitalize():  # Capitalize to match format
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the workweek")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Just a regular day")
