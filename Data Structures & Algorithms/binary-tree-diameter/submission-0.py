# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self, root):
        if root is None:
            return (0, 0)
        
        dia1, dep1 = self.helper(root.left)
        dia2, dep2 = self.helper(root.right)

        dep = max(dep1, dep2) + 1
        dia = max(dep1+dep2, max(dia1, dia2))

        return (dia, dep)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia, dep = self.helper(root)
        return dia
        