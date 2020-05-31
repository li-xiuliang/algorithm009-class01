"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def pre(root, res):
            if root is None:
                return None
            res.append(root.val)
            for c in root.children:
                pre(c, res)

        res = []
        pre(root, res)
        return res