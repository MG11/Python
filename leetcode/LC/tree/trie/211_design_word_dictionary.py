# https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/1725327/javacpython-a-very-well-detailed-explana-rcnm/


class TreeNode:
    def __init__(self):
        self.endOfWord = False
        self.data = defaultdict(TreeNode)

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()

    def addWord(self, word: str) -> None:
        dummyNode = self.root

        for w in word:
            if not dummyNode.data.get(w):
                dummyNode.data[w] = TreeNode()
            dummyNode = dummyNode.data[w]
        dummyNode.endOfWord = True
    
    def searchHelper(self, word, node):
        tempNode = node
        for i in range(len(word)):
            if word[i] == '.':
                for value in tempNode.data.values():
                    if self.searchHelper(word[i + 1:], value):
                        return True
                else:
                    return False
            else:
                if tempNode.data.get(word[i]):
                    tempNode = tempNode.data[word[i]]
                else:
                    return False
        return tempNode.endOfWord

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

------------------------------------------------------------------------------------------


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
