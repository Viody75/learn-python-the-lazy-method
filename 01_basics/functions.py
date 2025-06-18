# functions.py

"""
Python Functions Overview

Key Points:
- Functions use `def` keyword.
- No need to declare return types (but type hints are supported).
- Supports default, keyword, variable-length, and lambda arguments.
"""

# === Basic Function ===
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# === Default Arguments ===
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 3^2 = 9
print(power(3, 3))   # 3^3 = 27

# === Keyword Arguments ===
def describe_pet(name, animal="dog"):
    print(f"{name} is a {animal}")

describe_pet("Max")
describe_pet(animal="cat", name="Luna")  # order can be changed

# === Type Hints ===
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(4, 5))

# === Variable-length Arguments ===
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))  # *args → tuple of all values

def print_kv(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kv(name="Alice", age=30)

# === Lambda Expressions ===
double = lambda x: x * 2
print(double(5))

# === Functions Are First-Class Citizens ===
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(style, text):
    return style(text)

print(speak(shout, "Hello"))
print(speak(whisper, "Hello"))

# === Nested Functions ===
def outer(x):
    def inner(y):
        return x + y
    return inner

adder = outer(10)
print(adder(5))  # 15