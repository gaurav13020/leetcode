# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        r = preorder[0]
        index = 0
        
        index = inorder.index(preorder[0])
        
        node = TreeNode(r)
        node.left = self.buildTree(preorder[1:index+1], inorder[0:index])
        node.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        
        return node