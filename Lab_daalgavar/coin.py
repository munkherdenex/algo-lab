class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] > amount else dp[amount]

solution = Solution()
print(solution.coinChange([1, 2, 5], 11))  
print(solution.coinChange([2], 3))          