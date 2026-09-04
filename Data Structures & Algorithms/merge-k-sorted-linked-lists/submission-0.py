# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []

        head = ListNode(-1)
        curr = head

        k = len(lists)

        for i in range(k):
            if lists[i] is not None:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        while len(pq):
            val, i, node = heapq.heappop(pq)

            lists[i] = lists[i].next

            node.next = None
            curr.next = node
            curr = node

            if lists[i] is not None:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        return head.next
        
