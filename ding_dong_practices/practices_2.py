# Ding Dong Practice 2
# Recursion and Nested Loops
# Refer to SoalPraktikum2.pdf for the questions.

# 2.a. Recursion to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n * factorial(n - 1)  # recursive step

# Run it
# print("Factorial of 5 is:", factorial(5))  # 120

# 2.b. Recursion to solve Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:  # base case
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)  # move n-1 disks
    print(f"Move disk {n} from {source} to {target}")  # move nth disk
    tower_of_hanoi(n - 1, auxiliary, target, source)  # move n-1 disks

# Run it
# tower_of_hanoi(3, 'A', 'C', 'B')