# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, node, k):
        curr = node
        prev = None

        for i in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptrs = []

        curr = head

        flag = False
        while curr:
            ptrs.append(curr)
            for i in range(k):
                if curr is None:
                    flag = True
                    break
                curr = curr.next
            
        rem = None
        if flag:
            rem = ptrs.pop()
        
        for i in range(len(ptrs)):
            ptrs[i] = self.reverse(ptrs[i], k)
        
        res = ListNode(-1)
        temp = res
        for i in range(len(ptrs)):
            temp.next = ptrs[i]

            temp2 = ptrs[i]

            while temp2.next is not None:
                temp2 = temp2.next
            
            temp = temp2

        if rem is not None:
            temp.next = rem

        return res.next


