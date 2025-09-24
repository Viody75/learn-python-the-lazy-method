# Initialize a variable to demonstrate pass-by-value behavior
someVal = 0

# Function that modifies a parameter but doesn't return it
# This demonstrates that integers are passed by value in Python
def incByVal(initVal:int, val:int):
    initVal += val  # This modifies the local copy, not the original variable
    print(initVal)  # Prints the modified local value

# Function that decrements a parameter but doesn't return it
def decByVal(initVal:int, val:int):
    initVal -= val  # Again, this only modifies the local copy
    print(initVal)  # Prints the modified local value

# Call incByVal - this will print 5 (0 + 5)
incByVal(someVal, 5)
# But someVal remains unchanged because integers are immutable
print(someVal)  # This will still print 0

# Call decByVal - this will print -3 (0 - 3)
decByVal(someVal, 3)
# someVal is still unchanged
print(someVal)  # This will still print 0

# Functions that modify parameters AND return the result
# This is the correct way to modify values in Python
def incValByVal(initVal:int, val:int):
    initVal += val  # Modify the local copy
    return initVal  # Return the modified value

def decValByVal(initVal:int, val:int):
    initVal -= val  # Modify the local copy
    return initVal  # Return the modified value

# To actually change someVal, we need to assign the returned value
someVal = incValByVal(someVal, 5)  # someVal becomes 5 (0 + 5)
print(someVal)  # This will print 5

someVal = decValByVal(someVal, 3)  # someVal becomes 2 (5 - 3)
print(someVal)  # This will print 2

# Summary:
# - Immutable types (like int, float, str, tuple) are passed by value.
# - To modify them, you must return the new value and reassign it.
# - Mutable types (like list, dict, set) can be modified in place without returning