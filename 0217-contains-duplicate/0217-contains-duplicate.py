class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = set()
        for i in range(len(nums)):
            ans.add(nums[i])
        if len(ans) == len(nums):
            return False
        else:
            return True
        