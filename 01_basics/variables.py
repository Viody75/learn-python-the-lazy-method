# variables.py

"""
Python Variables for Experienced Devs

Key Points:
- Python is dynamically typed, so no need for 'let', 'var', or type declaration.
- Variable names are case-sensitive and snake_case by convention.
- Everything in Python is an object.
"""

# === Basic Declarations ===
a = 42                # int
b = 3.14              # float
c = "Hello"           # str
d = True              # bool
e = None              # null equivalent

print(a, b, c, d, e)

# === Multiple assignment ===
x, y = 10, 20
print(f"x={x}, y={y}")

# === Swapping variables (no temp var needed) ===
x, y = y, x
print(f"after swap: x={x}, y={y}")

# === Constants (convention only) ===
PI = 3.14159
GRAVITY = 9.8
# NOTE: Python doesn't enforce immutability for constants

# === Type Inference ===
# Python infers types at runtime
some_value = "abc"
print(type(some_value))  # <class 'str'>

# === Type Hints (optional but helpful) ===
username: str = "alice"
count: int = 10

# === Mutable vs Immutable ===
# Immutable types: int, float, str, tuple, bool, None
# Mutable types: list, dict, set, custom class

immutable_str = "hello"
# immutable_str[0] = "H"  # ❌ will raise TypeError

mutable_list = [1, 2, 3]
mutable_list[0] = 99       # ✅ allowed
print(mutable_list)

# === Identity vs Equality ===
a = [1, 2]
b = [1, 2]
print(a == b)      # True (value equality)
print(a is b)      # False (not same object in memory)

# === Dynamic Rebinding ===
x = 100
x = "now a string"
print(f"x is now: {x}")
