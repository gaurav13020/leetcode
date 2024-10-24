class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # return sum(range(len(nums) + 1)) - sum(nums) # One line version
        actualSum = 0
        for i in range(len(nums)):
            actualSum += nums[i]
            
        expectedSum = 0
        for i in range(len(nums)+1):
            expectedSum += i
            
        return expectedSum - actualSum
            