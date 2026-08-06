"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}
        res = Node(-1)
        temp = res
        curr = head
        while curr:
            node = Node(curr.val)

            temp.next = node

            map[curr] = node

            curr = curr.next
            temp = temp.next

        res = res.next
        curr = head

        while curr:
            map[curr].random = map[curr.random] if curr.random else None
            curr = curr.next
        return res
