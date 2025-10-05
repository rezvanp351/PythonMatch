# 🐍 Python Match Statement — Complete Beginner’s Tutorial

This repository teaches you how to use the **Python `match` statement** (available in Python 3.10+)  
with clear examples, step-by-step explanations, and practical use cases.

---

## 📘 What Is Match Statement?

The `match` statement allows Python to **choose between multiple options** depending on a value.  
It is similar to **switch-case** in other languages.

**Syntax:**
```python
match value:
    case option1:
        # code
    case option2:
        # code
    case _:
        # default code
```

---

## 🔹 Example 1: Simple Match
```python
value = 2
match value:
    case 1:
        print("Value is 1")
    case 2:
        print("Value is 2")  # This will print
    case _:
        print("Other value")
```

---

## 🔹 Example 2: Multiple Options in One Case
```python
fruit = "apple"
match fruit:
    case "apple" | "banana" | "orange":
        print("This is a common fruit")
    case "mango":
        print("This is a tropical fruit")
    case _:
        print("Unknown fruit")
```

---

## 🔹 Example 3: Tuple Pattern Matching
```python
point = (0, 1)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y} on Y-axis")
    case (x, 0):
        print(f"X={x} on X-axis")
    case (x, y):
        print(f"Point at ({x}, {y})")
```

---

## 🔹 Example 4: Dictionary Pattern Matching
```python
person = {"name": "Alice", "age": 25}
match person:
    case {"name": "Alice", "age": age}:
        print(f"Alice is {age} years old")
    case {"name": name}:
        print(f"Hello {name}")
    case _:
        print("Unknown person")
```

---

## 🔹 Example 5: Match with Guards (Conditions)
```python
number = 15
match number:
    case n if n % 2 == 0:
        print("Even number")
    case n if n % 2 != 0:
        print("Odd number")
```

---

## 🔹 Example 6: User Input with Match
```python
day = input("Enter a day (e.g., Monday): ")
match day.capitalize():
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the workweek")
    case "Saturday" | "Sunday":
        print("Weekend!")
    case _:
        print("Just a regular day")
```

---

## 💻 How to Run

1. Make sure you have **Python 3.10+** installed.
2. Clone this repository:
```bash
git clone https://github.com/yourusername/python-match-tutorial.git
```
3. Navigate to the project folder:
```bash
cd python-match-tutorial
```
4. Run the Python file:
```bash
python match_examples.py
```

---

## 📎 Author
👩‍💻 Created by: Rezvan Panah  
📅 Year: 2025  
🎯 Purpose: Teaching Python match statement to beginners  

---

## 💖 Support & Feedback
If this repository helped you, please consider:
- ⭐ **Starring** the repo  
- 🗨️ **Commenting** your thoughts  
- 📢 **Sharing** it with others learning Python  

Your feedback motivates more free educational content!

### 🔖 Tags
#Python #MatchStatement #PythonTutorial #BeginnerPython #PatternMatching #Python3.10
