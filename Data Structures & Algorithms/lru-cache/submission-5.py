class LRUCache:

    class Node:
        def __init__(self, val, key):
            self.val = val
            self.next = None
            self.prev = None
            self.key = key
    
    def update(self, node):
        if node is self.tail:
            return

        if node is self.head:
            self.head = self.head.next

        next = node.next
        prev = node.prev

        if prev is not None:
            prev.next = next

        if next is not None:
            next.prev = prev

        node.next = None
        node.prev = self.tail
        self.tail.next = node

        self.tail = node

    def remove(self):
        del self.d[self.head.key]
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        if self.head is None:
            self.tail = None
        

    def __init__(self, capacity: int):
        self.d = {}
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.d:
            self.update(self.d[key])
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.update(self.d[key])
            self.d[key].val = value
            return
        
        if self.capacity == len(self.d):
            self.remove()
        
        newNode = self.Node(value, key)
        self.d[key] = newNode

        if self.head is None:
            self.head = self.tail = newNode
            return
        
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode

