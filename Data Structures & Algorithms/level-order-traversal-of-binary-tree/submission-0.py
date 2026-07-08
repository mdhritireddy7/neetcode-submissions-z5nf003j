# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        currNode = root
        result = []
        queue = deque()

        queue.append(currNode)

        while queue:
            qLen = len(queue)
            level = []

            for i in range(qLen):
                currNode = queue.popleft()
                if currNode:
                    level.append(currNode.val)
                    queue.append(currNode.left)
                    queue.append(currNode.right)
            
            if level:
                result.append(level)

        return result



