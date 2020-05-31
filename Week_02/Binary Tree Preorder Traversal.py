# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        stack = [root]
        res = []

        while stack:
            tmp = stack.pop()
            res.append(tmp.val)
            if tmp.right is not None:
                stack.append(tmp.right)
            if tmp.left is not None:
                stack.append(tmp.left)
        return res