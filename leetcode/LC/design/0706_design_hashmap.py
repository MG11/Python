class Node:
    
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.arr = [Node()]*997

    def put(self, key: int, value: int) -> None:
        idx = key%997
        curr = self.arr[idx]
        while True:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                break
            curr = curr.next
        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        idx = key%997
        curr = self.arr[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        idx = key%997
        curr = self.arr[idx]
        while curr:
            if curr.next and curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)