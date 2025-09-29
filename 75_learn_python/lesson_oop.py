# lesson 1
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