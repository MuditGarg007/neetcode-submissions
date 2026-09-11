# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None:
            return None
        
        if root.val == p.val:
            return p
        
        if root.val == q.val:
            return q

        if (root.val>p.val and root.val<q.val) or (root.val<p.val and root.val>q.val):
            return root

        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return None
        