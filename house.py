class Solution:
    def rob(self, nums):
        memo = [-1] * len(nums)  
        return self.robHelper(nums, len(nums) - 1, memo)

    def robHelper(self, nums, i, memo):
        if i < 0:
            return 0
        if i == 0:
            return nums[0]

        if memo[i] != -1:
            return memo[i]

        memo[i] = max(self.robHelper(nums, i - 1, memo), self.robHelper(nums, i - 2, memo) + nums[i])
        return memo[i]

solution = Solution()
print(solution.rob([2, 7, 9, 3, 1]))  
print(solution.rob([1, 2, 3, 1]))     
