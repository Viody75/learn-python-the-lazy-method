print("\n=== Recursion: Factorial ===")

def faktorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    # recursive step
    return n * faktorial(n-1)

print("5! =", faktorial(5))  # 120

print("\n=== Recursion: Fibonacci ===")

def fibonacci(n):
    # base case
    if n == 0: return 0
    if n == 1: return 1
    # recursive step
    return fibonacci(n-1) + fibonacci(n-2)

# Cetak 6 angka pertama
hasil = [fibonacci(i) for i in range(6)]
print("Fibonacci 0–5:", hasil)  # [0, 1, 1, 2, 3, 5]

print("\n=== Recursion: Nested List Traversal ===")

nested = [1, [2, 3], [4, [5, 6]]]

def traverse(data):
    for item in data:
        if isinstance(item, list):
            traverse(item)   # recursive call
        else:
            print("Item:", item)

traverse(nested)
