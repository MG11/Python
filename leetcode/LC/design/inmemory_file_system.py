"""
https://leetcode.com/problems/design-in-memory-file-system/solution/
"""
from typing import List
from collections import defaultdict

class Dir:
    
    def __init__(self):
        self.files = defaultdict(str)
        self.dirs = defaultdict(Dir)
        
class FileSystem:

    def __init__(self):
        self.root = Dir()
        
    def __find_location(self, path):
        currentDir = self.root 
        pathArray = path.split('/')
        for p in range(1, len(pathArray) -1):
            currentDir = currentDir.dirs.get(pathArray[p])
        return currentDir, pathArray[-1]
        
        
    def ls(self, path: str) -> List[str]:
        data = []
        lastLocation, lastData = self.__find_location(path)
        if lastLocation.files.get(lastData):
            data.append(lastData)
            return data
        elif lastData != '' and lastLocation.dirs.get(lastData):
            lastLocation = lastLocation.dirs.get(lastData)
        data.extend(lastLocation.files.keys())
        data.extend(lastLocation.dirs.keys())
        data.sort()
        return data
            
    def mkdir(self, path: str) -> None:
        pathArray = path.split('/')
        currentDir = self.root
        for i in range(1, len(pathArray)):
            if currentDir.dirs.get(pathArray[i]):
                currentDir = currentDir.dirs.get(pathArray[i])
            else:
                newDir = Dir()
                currentDir.dirs[pathArray[i]] = newDir
                currentDir = newDir
        return
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        lastLocation, lastData = self.__find_location(filePath)
        lastLocation.files[lastData] += content
        
    def readContentFromFile(self, filePath: str) -> str:
        lastLocation, lastData = self.__find_location(filePath)
        if lastLocation.files.get(lastData):
            return lastLocation.files[lastData]
        else:
            return None
