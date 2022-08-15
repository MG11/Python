# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
        """

class NestedIterator:

    def __init__(self, nestedList):
        self.my_list = []
        def createList(nestedList):
            for element in nestedList:
                if element.isInteger():
                    a = element.getInteger()
                    print(a)
                    self.my_list.append(a)
                else:
                    createList(element.getList())
             
        createList(nestedList)
        self.start = 0
        
                
                
    def next(self) -> int:
        self.start += 1
        return self.my_list[self.start - 1]
    
    
    def hasNext(self) -> bool:
        return (self.start < len(self.my_list))
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
