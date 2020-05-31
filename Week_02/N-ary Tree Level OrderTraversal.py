"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root is None:
            return None

        previous_layer = [root]
        res = []

        while previous_layer:
            current_layer = []
            res.append([])
            for node in previous_layer:
                res[-1].append(node.val)
                current_layer.extend(node.children)
            previous_layer = current_layer
        return res