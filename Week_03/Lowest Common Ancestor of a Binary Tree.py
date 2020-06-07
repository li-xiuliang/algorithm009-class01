# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root in (None, p, q):
            return root
        
        stack = [root]

        while stack:
            node = stack.pop()
            if node.left or node.right:
                stack.append(node.left)
                stack.append(node.right)
            elif node.left:
                return node.left
            else:
                return node.right