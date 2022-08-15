"""
LC 146
take dict to store key and node 
take doubly LL to store value
take two head and tail pointers
"""

class DoublyLinkedList:
    
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoublyLinkedList()
        self.tail = DoublyLinkedList()
        self.hashmap = dict()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def __remove_node(self, node):
        # remove node from current position
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def __add_node(self, node):
        # add node at beginning
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node
    
    def __move_to_start(self, node):
        self.__remove_node(node)
        self.__add_node(node)
        
    def get(self, key: int) -> int:
        # if not node, return -1
        # else move to start (remove node, add node), return value
        if not self.hashmap.get(key):
            return -1
        node = self.hashmap[key]
        self.__move_to_start(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        # if node already exists, change value move to start
        # else, if capacity is full --> remove tail(remove node) --> add node
        #       else add node
        if self.hashmap.get(key):
            node = self.hashmap[key]
            node.value = value
            self.__move_to_start(node)
        else:
            # capacity is full remove tail
            if(len(self.hashmap) == self.capacity):
                prev = self.tail.prev
                self.__remove_node(prev)
                del self.hashmap[prev.key]
            node = DoublyLinkedList(key, value)
            self.__add_node(node)
            self.hashmap[key] = node
            
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)