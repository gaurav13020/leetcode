class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit =  prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r = r + 1
        return maxProfit
    # l, r = 0, 1
    #     maxP = 0
    #     while r < len (prices):
    #         if prices[1] < prices[r]:
    #             profit = prices[r] - prices[l]
    #             maxP = max (maxP, profit)
    #         else:
    #              l = r
    #         r += 1
    #     return maxP
        
        
        
        
        