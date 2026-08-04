# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find the mid:

        slow = head
        fast = head
        prev = None
        nxt = slow.next

        while fast and fast.next:
            prev = slow
            slow = slow.next
            nxt = slow.next
            fast = fast.next.next
        
        # reverse the second half
        curr = slow
        curr.next = prev
        prev = curr
        curr = nxt

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        p1 = head
        p2 = prev

        while (not p1 is p2) and (not p1.next is p2) and (not p2.next is p2):
            next1 = p1.next
            next2 = p2.next

            p1.next = p2
            p2.next = next1

            p1 = next1
            p2 = next2
        
        if p1 is p2:
            p1.next = None
        else:
            p1.next = p2
            p2.next = None
 
        


