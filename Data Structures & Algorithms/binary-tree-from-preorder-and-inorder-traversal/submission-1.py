# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def util(self, preorder, inorder, l, r):
        if(l>r):
            return None
        
        val = preorder[self.idx]
        self.idx+=1


        node = TreeNode(val)
        m=self.ind[val]

        leftSubtree = self.util(preorder, inorder, l, m-1)
        rightSubtree = self.util(preorder, inorder, m+1, r)

        node.left = leftSubtree
        node.right = rightSubtree

        return node
        
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.ind = {}

        for i in range(0, len(inorder)):
            self.ind[inorder[i]] = i

        
        self.idx = 0
        return self.util(preorder, inorder, 0, len(inorder)-1)
        


        