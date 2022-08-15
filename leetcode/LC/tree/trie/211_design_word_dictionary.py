from collections import defaultdict

class WordDictionary:
    
    def __init__(self):
        self.end = False
        self.data = defaultdict(WordDictionary)
        

    def addWord(self, word: str) -> None:
        Node = self
        for w in word:
            if Node.data.get(w):
                Node = Node.data.get(w)
            else:
                newNode = WordDictionary()
                Node.data[w] = newNode
                Node = newNode
        Node.end = True
        

    def search(self, word: str) -> bool:
        Node = self
        for w in range(len(word)):
            if Node and word[w] != '.':
                Node = Node.data.get(word[w], None)
            elif Node:
                for d in Node.data.keys():
                    if Node.data[d].search(word[w+1:]):
                        return True
                return False
            else:
                return False
        return Node and Node.end   
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)