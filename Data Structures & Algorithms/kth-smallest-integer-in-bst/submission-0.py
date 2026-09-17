# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def util(self, root, k):
        if root is None:
            return -1
        
        l = self.util(root.left, k)
        if l != -1:
            return l

        self.i += 1
        if self.i == k:
            return root.val
        
        r = self.util(root.right, k)
        if r!= -1:
            return r
        
        return -1


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        return self.util(root, k)