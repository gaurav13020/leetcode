# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.prev = None  # To keep track of the previous node
        
        def dfs(node):
            if not node:
                return
            
            # Store the right subtree temporarily
            right_subtree = node.right
            
            # Modify the node's pointers
            if self.prev:
                self.prev.right = node
                self.prev.left = None
            self.prev = node
            
            # Recursively flatten left and right subtrees
            dfs(node.left)
            dfs(right_subtree)
        
        dfs(root)   
        # current = root
        # while current:
        #     if current.left:
        #         temp = current.left
        #         while temp.right:
        #             temp = temp.right
        #         temp.right = current.right
        #         current.right = current.left
        #         current.left = None
        #     current = current.right   
        