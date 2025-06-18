# sets_tuples.py

"""
Python Sets & Tuples

Key Points:
- set: unordered collection of unique elements.
- tuple: immutable ordered collection.
"""

# === SET ===
# Unordered, mutable, no duplicates

s = {1, 2, 3, 2}
print(s)  # duplicates removed → {1, 2, 3}

# Add & Remove
s.add(4)
s.discard(2)
print(s)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # union: {1, 2, 3, 4, 5}
print(a & b)   # intersection: {3}
print(a - b)   # difference: {1, 2}
print(a ^ b)   # symmetric difference: {1, 2, 4, 5}

# Membership
print(1 in a)

# Convert from list to set
nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
print(unique_nums)

# === TUPLE ===
# Ordered, immutable

t = (10, 20, 30)
print(t[0])

# Single-element tuple needs comma!
one_item = (42,)
print(type(one_item))  # <class 'tuple'>

# Tuple unpacking
x, y, z = t
print(f"x={x}, y={y}, z={z}")

# Useful for returning multiple values
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 7])
print(f"min={lo}, max={hi}")

# Tuples can be keys in dicts (because they’re immutable)
coords = {(0, 0): "origin", (1, 2): "point"}
print(coords[(1, 2)])
