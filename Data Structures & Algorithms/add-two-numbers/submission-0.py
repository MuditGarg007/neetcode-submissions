# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = l1
        p2 = l2
        carry = 0
        res = ListNode(-1)
        tmp = res
        while p1 is not None and p2 is not None:
            s = p1.val + p2.val + carry
            carry = s//10
            node = ListNode(s%10)

            tmp.next = node
            tmp = tmp.next
            p1 = p1.next
            p2 = p2.next
        
        while p1 is not None:
            s = p1.val + carry
            carry = s//10
            node = ListNode(s%10)
            tmp.next = node
            p1 = p1.next
            tmp = tmp.next
        
        while p2 is not None:
            s = p2.val + carry
            carry = s//10
            node = ListNode(s%10)
            tmp.next = node
            p2 = p2.next
            tmp = tmp.next
        
        while carry:
            node = ListNode(carry%10)
            carry = carry//10
            tmp.next = node


        return res.next