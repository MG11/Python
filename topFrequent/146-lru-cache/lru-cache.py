class DoublyLinkedList:

    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoublyLinkedList(-1, -1)
        self.tail = DoublyLinkedList(-1, -1)
        self.capacity = capacity
        self.data = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def moveFront(self, node):
        #detatch
        prevNode = node.prev
        nextNode = node.next
        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode

        nextNode = self.head.next
        nextNode.prev = node
        node.next = nextNode
        self.head.next = node
        node.prev = self.head
    
    def deleteLast(self):
        temp = self.tail.prev
        if not temp or temp == self.head:
            return
        temp.prev.next = self.tail
        self.tail.prev = temp.prev
        self.data.pop(temp.key)
        del temp

    def get(self, key: int) -> int:
        data = self.data
        if not data.get(key, None):
            return -1
        node = data[key]
        self.moveFront(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        data = self.data
        if data.get(key):
            node = data[key]
            node.val = value
        else:
            if len(data) >= self.capacity:
                self.deleteLast()
            node = DoublyLinkedList(key, value)
            data[key] = node
        self.moveFront(node)        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)