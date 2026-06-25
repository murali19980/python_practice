"""
Practice: Dynamic Programming
Goal: Optimize recursion with memoization & tabulation.
"""

# 1. Fibonacci (Memoization)
def fib_memo(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

# 2. Fibonacci (Tabulation - Bottom Up)
def fib_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 3. Coin Change (Minimum coins to make amount)
def coin_change(coins, amount):
    # dp[i] = min coins to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    print(f"Fib(10) Memo: {fib_memo(10)}")
    print(f"Fib(10) Tab: {fib_tab(10)}")
    print(f"Min coins for 11 using [1,5,6]: {coin_change([1,5,6], 11)}")  # 5+6 = 2 coins
