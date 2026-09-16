# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def util(self, root, max, min):
        if not root:
            return True

        if root.val<=min or root.val>=max:
            return False

        return self.util(root.left, root.val, min) and self.util(root.right, max, root.val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.util(root, float('inf'), float('-inf'))