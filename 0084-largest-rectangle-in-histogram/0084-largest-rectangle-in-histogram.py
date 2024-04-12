class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxValue = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                
                index, height = stack.pop()
                maxValue = max(maxValue, height*(i-index))
                start = index
            stack.append((start, h))
        for i, h in stack:
            maxValue = max(maxValue, h*(len(heights)-i))
        return maxValue