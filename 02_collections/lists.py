# lists.py

"""
Python Lists: A Powerful Built-in Collection

Key Points:
- Lists are dynamic arrays (mutable, ordered).
- Elements can be any type (mixed types allowed).
- Supports slicing, iteration, and comprehension.
"""

# === Declaration ===
nums = [1, 2, 3, 4]
mixed = [1, "hello", True, 3.14]

print(nums)
print(mixed)

# === Accessing Elements ===
print(nums[0])      # first element
print(nums[-1])     # last element

# === Slicing ===
print(nums[1:3])    # elements at index 1 and 2
print(nums[:2])     # first 2 elements
print(nums[::2])    # every 2 steps

# === Modifying Lists ===
nums[0] = 100
print(nums)

# === Adding Elements ===
nums.append(5)
nums.insert(1, 200)   # insert at index 1
print(nums)

# === Removing Elements ===
nums.remove(200)      # remove first matching value
last = nums.pop()     # remove and return last element
print(f"popped: {last}, now: {nums}")

# === Checking Membership ===
print(3 in nums)      # True or False

# === Iteration ===
for num in nums:
    print(f"num: {num}")

# === List Comprehension ===
squares = [n**2 for n in range(5)]
print(squares)

# === Built-in Functions ===
print(len(nums))      # length
print(min(nums))      # min value
print(max(nums))      # max value
print(sorted(nums))   # returns a sorted copy

# === Copying Lists (⚠️ Don't just use `=`) ===
a = [1, 2, 3]
b = a           # ❌ reference, not copy
b[0] = 999
print(f"original a: {a}, modified b: {b}")

# Correct way to copy:
c = a.copy()    # ✅ shallow copy
c[0] = 123
print(f"after copy: a={a}, c={c}")
