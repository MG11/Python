class Trie:

    def __init__(self):
        self.val = None
        self.children = {}
        self.isend = False
        

    def insert(self, word: str) -> None:
        root = self
        for w in word:
            t = root.children.get(w)
            if not t:
                t = Trie()
                t.val = w
                root.children[w] = t
            root = t
        root.isend = True

    def search(self, word: str) -> bool:
        start = self
        for w in word:
            if not start.children.get(w):
                return False
            start = start.children[w]
        return start.isend

    def startsWith(self, prefix: str) -> bool:
        start = self
        for w in prefix:
            if not start.children.get(w):
                return False
            start = start.children[w]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)