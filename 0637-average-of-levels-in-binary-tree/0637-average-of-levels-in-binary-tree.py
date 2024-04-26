# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []
        if root == None:
            return answer
        
        queue = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            currentLevel = []
            average = 0.0
            for i in range(size):
                currentNode = TreeNode()
                currentNode = queue.pop(0)
                average = average + currentNode.val
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            answer.append(average/size)
        return answer