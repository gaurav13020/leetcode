class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in numsSet:
            if (num - 1) not in numsSet:
                maxL = 1
                while (num + maxL) in numsSet:
                    maxL += 1
                longest = max(longest, maxL)
        return longest
