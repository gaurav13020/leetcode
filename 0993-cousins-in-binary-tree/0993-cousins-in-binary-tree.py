# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
    
        def findNode(node, x):
            if not node:
                return None
            if node.val == x:
                return node
            n = findNode(node.left, x)
            if n:
                return n
            return findNode(node.right, x)
        
        def isSibling(node, x, y):
            if not node:
                return False
            return (node.left == x and node.right == y) or (node.left == y and node.right == x) or isSibling(node.left, x, y) or isSibling(node.right, x, y)
        def level(node, x, i):
            if not node:
                return 0
            if node == x:
                return i
            l = level(node.left, x, i+1)
            if l != 0:
                return l
            l = level(node.right, x, i+1)
            return l
        
        
        xx = findNode(root, x)
        yy = findNode(root, y)
        
        return (level(root, xx, 0) == level(root, yy, 0)) and not isSibling(root, xx, yy)