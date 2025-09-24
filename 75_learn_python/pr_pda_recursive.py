def solve_toh(n, source, target, temporary):
    # Base case
    if n == 1:
        print(f"Pindahkan cakram 1 dari {source} ke {target}")
        return

    # Step 1: pindahkan n-1 cakram dari source ke auxiliary
    solve_toh(n-1, source, temporary, target)

    # Step 2: pindahkan 1 cakram terakhir dari source ke target
    print(f"Pindahkan cakram {n} dari {source} ke {target}")

    # Step 3: pindahkan n-1 cakram dari auxiliary ke target
    solve_toh(n-1, temporary, target, source)

# Testing untuk 5 cakram
solve_toh(5, "A", "C", "B")