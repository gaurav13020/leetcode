# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def dfs(root, k):
            if not root:
                return None
        
            left = dfs(root.left, k)
        
            
        
            self.count += 1
            if self.count == k:
                return root
            if left:
                return left
            
            return dfs(root.right, k)
        
        
        return dfs(root, k).val
    