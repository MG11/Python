# https://leetcode.com/problems/implement-trie-prefix-tree/

from collections import defaultdict

class Trie:
    
    def __init__(self):
        self.end = False
        self.data = defaultdict(Trie)
        
    def insert(self, word: str) -> None:
        Node = self
        for w in word:
            if Node.data.get(w):
                Node = Node.data.get(w)
                continue
            else:
                newNode = Trie()
                Node.data[w] = newNode
                Node = newNode
        Node.end = True
        
    def search(self, word: str) -> bool:
        Node = self
        for w in word:
            if Node:
                Node = Node.data.get(w, None)
        return Node and Node.end        
            

    def startsWith(self, prefix: str) -> bool:
        Node = self
        for w in prefix:
            if Node:
                Node = Node.data.get(w, None)
        return Node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
