"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        return self.helper(root, [])

    def helper(self, node, result):
        if not node:
            return []

        for c in node.children:
            self.helper(c, result)

        result.append(node.val)

        return result
        
        