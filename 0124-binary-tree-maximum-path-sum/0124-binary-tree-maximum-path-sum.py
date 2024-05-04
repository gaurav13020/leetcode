# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = -2147483648
        
        def dfs(node):
            
            if not node:
                return 0
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            
            leftHeight = max(0, leftHeight)
            rightHeight = max(0, rightHeight)
            
            curSum = leftHeight + rightHeight + node.val
            
            
            self.sum = max(self.sum, curSum)
            
            return max(leftHeight, rightHeight) + node.val
        
        
        dfs(root)
        return self.sum