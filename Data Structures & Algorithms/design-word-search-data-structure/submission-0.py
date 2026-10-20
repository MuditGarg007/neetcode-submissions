class WordDictionary:

    class Node:
        def __init__(self, val):
            self.val = val
            self.children = {}
            self.terminal = False

    def __init__(self):
        self.head = self.Node('0')
        

    def addWord(self, word: str) -> None:
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
        
        def rec(temp, word, i):
            if i==len(word):
                if temp.terminal:
                    return True
                else:
                    return False

            if word[i] == '.':
                for child in temp.children:
                    if rec(temp.children[child], word, i+1):
                        return True

            elif word[i] in temp.children:
                temp = temp.children[word[i]]
                return rec(temp, word, i+1)

            return False

        return rec(temp, word, 0)

        
