# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.postorderDFS(root, [])


    def postorderDFS(self, node, result):
        if not node:
            return []

        if node.left:
            self.postorderDFS(node.left, result)

        if node.right:
            self.postorderDFS(node.right, result)

        result.append(node.val)
        return result        