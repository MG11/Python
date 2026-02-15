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


/// latest solution:

from collections import defaultdict

class TrieNode:

    def __init__(self):
        self.endOfWord = False
        self.data = defaultdict(TrieNode)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        tempNode = self.root

        for w in word:
            if not tempNode.data.get(w):
                tempNode.data[w] = TrieNode()
            tempNode = tempNode.data[w]
        tempNode.endOfWord = True


    def search(self, word: str) -> bool:
        tempNode = self.root

        for w in word:
            if tempNode.data.get(w):
                tempNode = tempNode.data[w]
            else:
                return False
        return tempNode.endOfWord

    def startsWith(self, prefix: str) -> bool:
        tempNode = self.root

        for w in prefix:
            if tempNode.data.get(w):
                tempNode = tempNode.data[w]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
