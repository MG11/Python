class DoublyLinkedList:
    def __init__(self, key, val, prev= None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.head = DoublyLinkedList(-1, -1, None, None)
        self.tail = DoublyLinkedList(-1, -1, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.data = {}

    def deleteLast(self):
        temp = self.tail.prev
        if temp is None or temp == self.head:
            return
        self.tail.prev = temp.prev
        temp.prev.next = self.tail
        self.data.pop(temp.key, None)
        del temp

    def moveFront(self, node):

        ## detach first
        prevNode = node.prev
        nextNode = node.next
        if prevNode:
            prevNode.next = nextNode
        if nextNode:
            nextNode.prev = prevNode

        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node

    def get(self, key: int) -> int:
        node = self.data.get(key)
        if not node:
            return -1
        else:
            self.moveFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.data.get(key, None):
            node = self.data.get(key)
            node.val = value
            self.moveFront(node)
            return node.val
        if len(self.data) >= self.capacity:
            self.deleteLast()
        node = DoublyLinkedList(key, value)
        self.data[key] = node
        self.moveFront(node)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)