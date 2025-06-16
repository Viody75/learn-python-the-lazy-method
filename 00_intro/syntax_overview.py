# syntax_overview.py
"""
Basic Python Syntax Overview

This file gives a compact overview of core Python syntax,
written for devs familiar with other languages (e.g. JavaScript, Java, C++).
"""

# === 1. Comments ===
# Single-line comments use '#'
"""Multi-line docstrings can be triple double-quotes (or single)."""

# === 2. Variables ===
x = 10           # dynamic typing, no 'let' or 'var'
pi = 3.14
name = "Alice"
is_active = True

# === 3. Data Types ===
num = 42                     # int
flt = 3.14                   # float
txt = "hello"                # str
flag = False                 # bool
lst = [1, 2, 3]              # list (array)
tup = (1, 2, 3)              # tuple (immutable)
dct = {"key": "value"}       # dict (map)
st = {1, 2, 3}               # set (unique elements)

# === 4. Conditionals ===
if x > 5:
    print("x is big")
elif x == 5:
    print("x is five")
else:
    print("x is small")

# === 5. Loops ===
for item in lst:
    print(item)

while x > 0:
    x -= 1

# === 6. Functions ===
def greet(name):
    return f"Hello, {name}!"

# === 7. Classes & OOP ===
class Animal:
    def __init__(self, name):   # constructor
        self.name = name        # instance variable

    def speak(self):
        print(f"{self.name} makes a sound.")

dog = Animal("Dog")
dog.speak()

# === 8. Exceptions ===
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Cannot divide by zero")
finally:
    print("Always runs")

# === 9. List Comprehensions ===
squares = [n**2 for n in range(5)]  # [0, 1, 4, 9, 16]

# === 10. Importing Modules ===
import math
print(math.sqrt(16))

# === 11. With Statement (context manager) ===
with open("somefile.txt", "w") as f:
    f.write("hello")
# auto-closes the file, like 'using' in C#

# === 12. Lambda Functions ===
add = lambda a, b: a + b
print(add(2, 3))

# === 13. Type Hints (Optional but good) ===
def add_nums(a: int, b: int) -> int:
    return a + b

# === 14. Main Check ===
if __name__ == "__main__":
    print("This runs only if file is executed directly.")
