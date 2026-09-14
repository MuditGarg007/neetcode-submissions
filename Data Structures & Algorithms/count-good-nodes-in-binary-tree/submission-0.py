# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def util(self, root, maxNode):
        if not root:
            return count
        
        if root.val>=maxNode:
            self.count += 1
        
        maxNode = max(maxNode, root.val)

        self.util(root.left, maxNode)
        self.util(root.right, maxNode)
        
    
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.count = 0
        self.util(root, root.val)
        return self.count

        