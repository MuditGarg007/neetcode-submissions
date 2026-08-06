# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        temp = head

        while temp is not None:
            temp = temp.next
            length+=1
        
        idx = length - n

        curr = head
        prev = None
        nxt = head.next
        for i in range(0, idx-1):
            prev = curr
            curr = curr.next
            nxt = curr.next

        if prev:
            prev.next = nxt
        else:
            head = head.next

        return head