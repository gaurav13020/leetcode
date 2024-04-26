# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if root == None:
            return answer
        
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            currentLevel = []
            for i in range(size):
                currentNode = TreeNode()
                currentNode = queue.pop(0)
                currentLevel.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            answer.append(currentLevel)
        return answer[::-1]