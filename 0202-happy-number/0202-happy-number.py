class Solution:
    def isHappy(self, n: int) -> bool:
        def findSquare(n):
            ans = 0
            while n > 0:
                rem = n%10
                ans += rem *rem
                n = n//10
                
            return ans
        
        fast = n
        slow = n
        while True:
            slow = findSquare(slow)
            fast = findSquare(findSquare(fast))
            if fast == slow:
                break
        if slow == 1:
            return True
        return False
        
        