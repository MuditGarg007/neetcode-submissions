class PrefixTree:

    class Node:
        def __init__(self, val):
            self.val = val
            self.children = []
            self.terminal = False
            

    def __init__(self):
        self.head = self.Node('0')

    def insert(self, word: str) -> None:
        temp = self.head
        for ch in word:
            flag = False
            for child in temp.children:
                if ch == child.val:
                    temp = child
                    flag = True
                    break

            if not flag:
                node = self.Node(ch)
                temp.children.append(node)
                temp = node

        temp.terminal = True


    def search(self, word: str) -> bool:
        temp = self.head

        for ch in word:
            flag = False
            for child in temp.children:
                if ch == child.val:
                    temp = child
                    flag = True
            if not flag:
                return False
        
        return temp.terminal
        

    def startsWith(self, prefix: str) -> bool:
        temp = self.head

        for ch in prefix:
            flag = False
            for child in temp.children:
                if ch == child.val:
                    temp = child
                    flag = True
            if not flag:
                return False
        
        return True
        
        