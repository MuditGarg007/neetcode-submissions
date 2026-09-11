# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return list()
        
        q = deque()
        q.append(None)
        q.append(root)


        res = []

        while q:
            node = q.popleft()

            if not node:
                if not q:
                    return res
                res.append(q[0].val)
                q.append(None)
                continue
            
            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)


        return res;
            


            




            