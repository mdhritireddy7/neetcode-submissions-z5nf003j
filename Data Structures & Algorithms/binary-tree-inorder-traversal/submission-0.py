# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.DFS(root, [])


    def DFS(self, node, result):
        if not node:
            return []
            
        if(node.left):
            self.DFS(node.left, result)
        
        result.append(node.val)

        if(node.right):
            self.DFS(node.right, result)

        return result
        