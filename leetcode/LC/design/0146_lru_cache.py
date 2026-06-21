class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        node = self.hashMap.get(key)
        self.remove(node)
        self.add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.hashMap.get(key):
            node = self.hashMap.get(key)
            self.remove(node)
            node.val = value
        else:
            if(len(self.hashMap) >= self.capacity):
                nodeToRemove = self.tail.prev
                self.remove(nodeToRemove)
                del self.hashMap[nodeToRemove.key]
            node = ListNode(key, value)
            self.hashMap[key] = node
        self.add_to_head(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
