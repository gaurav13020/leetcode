# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            
            if not node:
                return 0
            
            leftHeight = height(node.left)
            rightHeight = height(node.right)
            dia = leftHeight + rightHeight
            self.diameter = max(self.diameter, dia)
            
            return max(leftHeight, rightHeight) + 1
            
        height(root)
        return self.diameter
    