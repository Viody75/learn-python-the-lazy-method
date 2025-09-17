# Use Case: Tower of Hanoi Puzzle
#  Aturan:
# Ada 3 tiang (A, B, C).
# Semua cakram harus dipindah dari A → C.
# Hanya boleh pindahkan 1 cakram per langkah.
# Cakram besar tidak boleh ditaruh di atas cakram kecil.

print("\n=== Tower of Hanoi (Recursive) ===")

def hanoi(n, source, target, auxiliary):
    # Base case
    if n == 1:
        print(f"Pindahkan cakram 1 dari {source} ke {target}")
        return

    # Step 1: pindahkan n-1 cakram dari source ke auxiliary
    hanoi(n-1, source, auxiliary, target)

    # Step 2: pindahkan 1 cakram terakhir dari source ke target
    print(f"Pindahkan cakram {n} dari {source} ke {target}")

    # Step 3: pindahkan n-1 cakram dari auxiliary ke target
    hanoi(n-1, auxiliary, target, source)

# Testing untuk 3 cakram
hanoi(3, "A", "C", "B")

print("\n=== Tower of Hanoi (Iterative) ===")

def hanoi_iter(n, source, target, auxiliary):
    total_moves = 2**n - 1  # rumus jumlah langkah
    rods = {source: list(range(n, 0, -1)), target: [], auxiliary: []}

    # Jika jumlah cakram genap, tukar target dan auxiliary
    if n % 2 == 0:
        target, auxiliary = auxiliary, target

    for move in range(1, total_moves+1):
        if move % 3 == 1:
            src, dst = source, target
        elif move % 3 == 2:
            src, dst = source, auxiliary
        else:
            src, dst = auxiliary, target

        # pindahkan cakram antara dua tiang (aturan sederhana)
        if rods[src] and (not rods[dst] or rods[src][-1] < rods[dst][-1]):
            rods[dst].append(rods[src].pop())
            print(f"Pindahkan cakram {rods[dst][-1]} dari {src} ke {dst}")
        else:
            rods[src].append(rods[dst].pop())
            print(f"Pindahkan cakram {rods[src][-1]} dari {dst} ke {src}")

# Testing untuk 3 cakram
hanoi_iter(3, "A", "C", "B")

