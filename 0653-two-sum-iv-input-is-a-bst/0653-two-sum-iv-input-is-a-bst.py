# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        answer = {}
        def dfs (node):
            if not node:
                return False
            
            if k - node.val in answer:
                return True
            else:
                answer[node.val] = True
            return dfs(node.left) or dfs(node.right)
            
            
        return dfs(root)
        