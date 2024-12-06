def coin_change(coins, amount):
    memo = {}

    def dp(rem):
        if rem < 0:
            return float('inf')  
        if rem == 0:
            return 0  
        if rem in memo:
            return memo[rem]

        memo[rem] = min(dp(rem - coin) + 1 for coin in coins)
        return memo[rem]

    result = dp(amount)
    return result if result != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print("Minimum coins:", coin_change(coins, amount))
