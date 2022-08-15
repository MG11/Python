"""
LC 146
take dict to store key and node 
take doubly LL to store value
take two head and tail pointers
"""

class DoubleLinkedList:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = {}
        self.head = DoubleLinkedList(-1, -1)
        self.tail = DoubleLinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # if element is not in map return -1
        # move to it head and return its value
        if not self.my_dict.get(key):
            return -1
        node = self.my_dict[key]
        if node.prev == self.head:
            return node.val
        node.next.prev = node.prev
        node.prev.next = node.next
        self.move_to_start(node)
        return node.val
        
        
    def put(self, key: int, value: int) -> None:
        # if same element is there remove that
        # if size exausted, then remove..
        # insert at head
        if(self.my_dict.get(key)):
            self.remove(self.my_dict[key])
        if len(self.my_dict) == self.capacity:
            self.remove(self.tail.prev)
        self.insert(key, value)
        
    def insert(self, key, value):
        node = DoubleLinkedList(key, value)
        self.move_to_start(node)
        self.my_dict[key] = node
        
    def remove(self, node):
        # delete the node and manage pointers
        key = node.key
        del self.my_dict[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del node
    
    def move_to_start(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)