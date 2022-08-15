from collections import defaultdict
from typing import List

"""
https://leetcode.com/problems/design-in-memory-file-system/solution/
"""

class Dir:
    def __init__(self):
        self.dirs = defaultdict(Dir)
        self.files = defaultdict(str)

class FileSystem:

    def __init__(self):
        self.root = Dir()

    def ls(self, path: str) -> List[str]:
        t = self.root
        data = []
        if(path != '/'):
            pathArray = path.split('/')
            for i in range(1, len(pathArray) - 1):
                t = t.dirs.get(pathArray[i])
            if t.files.get(pathArray[-1]):
                data.append(pathArray[-1])
                return data
            else:
                t = t.dirs.get(pathArray[-1])
        data.extend(t.dirs.keys())
        data.extend(t.files.keys())
        data.sort()
        return data

    def mkdir(self, path: str) -> None:
        t = self.root
        pathArray = path.split('/')
        for i in range(1, len(pathArray)):
            if not t.dirs.get(pathArray[i]):
                m = Dir()
                t.dirs[pathArray[i]] = m
                t = m
            else:
                t = t.dirs.get(pathArray[i])

    def addContentToFile(self, filePath: str, content: str) -> None:
        t = self.root
        data = []
        pathArray = filePath.split('/')
        for i in range(1, len(pathArray) - 1):
            t = t.dirs.get(pathArray[i])
            print(t)
        if t.files.get(pathArray[-1]):
            t.files[pathArray[-1]] += content
        else:
            t.files[pathArray[-1]] = content
        

    def readContentFromFile(self, filePath: str) -> str:
        t = self.root
        data = []
        pathArray = filePath.split('/')
        for i in range(1, len(pathArray) - 1):
            t = t.dirs.get(pathArray[i])
        return t.files.get(pathArray[-1])
        
        
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)