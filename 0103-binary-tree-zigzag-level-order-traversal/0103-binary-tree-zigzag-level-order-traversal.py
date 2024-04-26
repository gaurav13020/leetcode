import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if root == None:
            return answer
        
        queue = collections.deque()
        queue.append(root)
        evenLevel = False
        while queue:
            size = len(queue)
            currentLevel = []
            
            
            
            if evenLevel:
                for i in range(size):
                    currentNode = TreeNode()
                    currentNode = queue.popleft()
                    currentLevel.append(currentNode.val)
                    if currentNode.right:
                        queue.append(currentNode.right)
                    if currentNode.left:
                        queue.append(currentNode.left)
                
            else:
                for i in range(size):
                    currentNode = TreeNode()
                    currentNode = queue.pop()
                    currentLevel.append(currentNode.val)
                    if currentNode.left:
                        queue.appendleft(currentNode.left)
                    if currentNode.right:
                        queue.appendleft(currentNode.right)
            evenLevel = not evenLevel       
                
            
                    
                    
            answer.append(currentLevel)
        return answer