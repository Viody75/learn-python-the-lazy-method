# ===============================================
# SOAL 4: Optimization Problem (Minimum Coin Change)
# ===============================================

# --- Brute Force (Recursive) ---
def min_coins_bruteforce(coins, target):
    if target == 0:
        return 0
    if target < 0:
        return float('inf')
    
    min_count = float('inf')
    for coin in coins:
        count = min_coins_bruteforce(coins, target - coin)
        if count != float('inf'):
            min_count = min(min_count, count + 1)
    return min_count


# --- Dynamic Programming (Bottom-Up) ---
def min_coins_dp(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    for i in range(1, target + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[target] if dp[target] != float('inf') else -1


# --- Pengujian Soal ---
cases = [
    {"coins": [25, 10, 5], "sum": 30},
    {"coins": [9, 6, 5, 1], "sum": 19},
    {"coins": [4, 6, 2], "sum": 5}
]

print("=== (a) Brute Force dan (b) Dynamic Programming ===")
for case in cases:
    coins, target = case["coins"], case["sum"]

    # Brute Force
    result_brute = min_coins_bruteforce(coins, target)
    if result_brute == float('inf'):
        result_brute = -1

    # Dynamic Programming
    result_dp = min_coins_dp(coins, target)

    print(f"Coins = {coins}, Target = {target}")
    print(f"  Brute Force -> {result_brute}")
    print(f"  DP          -> {result_dp}\n")
