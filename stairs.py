class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.memo:
            return self.memo[n]

        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)

        self.memo[n] = result

        return result

solution = Solution()
print(solution.climbStairs(2))
