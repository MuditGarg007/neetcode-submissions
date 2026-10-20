class PrefixTree:

    class Node:
        def __init__(self, val):
            self.val = val
            self.children = {}
            self.terminal = False
            

    def __init__(self):
        self.head = self.Node('0')

    def insert(self, word: str) -> None:
        temp = self.head
        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
                continue
            
            node = self.Node(ch)
            temp.children[ch] = node
            temp = node

        temp.terminal = True


    def search(self, word: str) -> bool:
        temp = self.head

        for ch in word:
            if ch in temp.children:
                temp = temp.children[ch]
                continue

            return False
        
        return temp.terminal
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.head

        for ch in prefix:
            if ch in temp.children:
                temp = temp.children[ch]
                continue
            return False
        
        return True
        
        