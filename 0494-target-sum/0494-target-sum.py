# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         if abs(target) > sum(nums): return 0  # nums = [10], target = -100
        
        
#         s1 = (target + sum(nums)) // 2
#         # 2 * s1 = (target + sum(nums))  => as (target + sum(nums)) is a multiple of 2 so it must be an even number
        
#         if (target + sum(nums)) % 2 != 0: return 0
        
#         memo = [[0]*(s1+1) for i in range(len(nums) + 1)]
        
        
        
        
#         def dp(arr, sum, n, memo):
#             if sum == 0:
#                 return 1
#             if n == 0:
#                 return 0
            
#             if memo[n][sum] != 0:
#                 return memo[n][sum]
            
#             if arr[n-1] <= sum or arr[n-1]==0:
#                 memo[n][sum] = dp(arr, sum-arr[n-1], n-1, memo) + dp(arr, sum, n-1, memo)
#             else:
#                 memo[n][sum] = dp(arr, sum, n-1, memo)
                
#             return memo[n][sum]
#         return dp(nums, s1, len(nums), memo)
        
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if abs(target) > sum(nums): return 0  # nums = [10], target = -100
        
        
        s1 = (target + sum(nums)) // 2
        # 2 * s1 = (target + sum(nums))  => as (target + sum(nums)) is a multiple of 2 so it must be an even number
        
        if (target + sum(nums)) % 2 != 0: return 0
        
        dp = [[0]*(s1+1) for i in range(len(nums) + 1)]
        
        for j in range(s1 + 1):
            dp[0][j] = 0
        for i in range(len(nums)+1):
            dp[i][0] = 1
        # change values of remaining dp starting from (1, 0) to (len(nums), s1)
        
        
        for i in range(1, len(nums) + 1):
            for j in range(s1 + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1] # dp[len(nums)][s1]
        