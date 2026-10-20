# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def util(self, node):
        if node is None:
            return 0
        l = self.util(node.left)
        r = self.util(node.right)
        self.maxSum = max(l+r+node.val, l+node.val, r+node.val, node.val, self.maxSum)

        return max(node.val, node.val+l, node.val+r)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')

        self.util(root)
        return self.maxSum