# Summary for lesson 1:
# - Immutable types (like int, float, str, tuple) are passed by value.
# - To modify them, you must return the new value and reassign it.
# - Mutable types (like list, dict, set) can be modified in place without returning

# Initialize a variable (immutable type: int)
someVal = 0

# Function that modifies a parameter but doesn't return it
# -> menunjukkan bahwa integer (immutable) tidak berubah di luar fungsi
def incByVal(initVal: int, val: int):
    initVal += val  # hanya mengubah copy lokal
    print(f"[incByVal] inside function: {initVal}")

def decByVal(initVal: int, val: int):
    initVal -= val  # hanya mengubah copy lokal
    print(f"[decByVal] inside function: {initVal}")


# --- Testing 1 ---
print("=== Pass-by-Value dengan Immutable (int) ===")
incByVal(someVal, 5)     # prints 5
print("outside:", someVal)  # tetap 0
decByVal(someVal, 3)     # prints -3
print("outside:", someVal)  # tetap 0

# Fungsi yang mengembalikan nilai baru
def incValByVal(initVal: int, val: int):
    initVal += val
    return initVal

def decValByVal(initVal: int, val: int):
    initVal -= val
    return initVal


# --- Testing 2 ---
print("\n=== Mengubah dengan Return (Immutable) ===")
someVal = incValByVal(someVal, 5)   # assign hasil
print("after incValByVal:", someVal)  # 5
someVal = decValByVal(someVal, 3)
print("after decValByVal:", someVal)  # 2