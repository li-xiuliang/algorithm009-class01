# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if len(preorder) == 0:
            return None
        dic = {k : v for v, k in enumerate(inorder)}
        
        def build(preorder_left, inorder_left, inorder_right):
            if inorder_right - inorder_left < 1:
                return
            root = TreeNode(preorder[preorder_left])
            mid = dic[preorder[preorder_left]]
            offset = mid - inorder_left

            root.left = build(preorder_left + 1, inorder_left, mid)
            root.right = build(preorder_left + offset + 1, mid + 1, inorder_right)

            return root
        root = build(0, 0, len(inorder))
        return root