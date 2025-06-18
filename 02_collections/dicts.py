# dicts.py

"""
Python Dictionaries: Key-Value Pair Collections

Key Points:
- Dicts are unordered (until Python 3.7+), mutable, and fast for lookups.
- Keys must be hashable (e.g. str, int, tuple), values can be anything.
- Very useful for JSON-like data structures.
"""

# === Declaration ===
person = {
    "name": "Alice",
    "age": 30,
    "is_active": True
}

print(person)

# === Accessing Values ===
print(person["name"])
# print(person["nonexistent"])  # ❌ KeyError

# Safer access:
print(person.get("nickname", "No nickname"))

# === Adding & Modifying ===
person["location"] = "Jakarta"
person["age"] = 31

# === Removing Entries ===
del person["is_active"]
location = person.pop("location")
print(f"Removed location: {location}")

# === Iterating Over Keys/Values ===
for key in person:
    print(f"{key} = {person[key]}")

for key, value in person.items():
    print(f"{key} => {value}")

# === Dictionary Comprehension ===
squares = {x: x**2 for x in range(5)}
print(squares)

# === Checking Existence ===
print("age" in person)         # True
print("gender" not in person)  # True

# === Merging Dictionaries ===
default = {"theme": "light", "lang": "en"}
user = {"theme": "dark"}

# Python 3.9+
merged = default | user
print(merged)

# Python < 3.9 alternative:
merged_old = {**default, **user}
print(merged_old)
