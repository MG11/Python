# https://leetcode.com/problems/lfu-cache/solutions/207673/python-concise-solution-detailed-explana-8f7d/?envType=company&envId=salesforce&favoriteSlug=salesforce-three-months

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append(self, node):
        nextNode = self.head.next
        node.next = nextNode
        node.prev = self.head
        self.head.next = node
        nextNode.prev = node
        self.size += 1
    
    def pop(self, node = None):
        if self.size == 0:
            return None
        if node is None:
            node = self.tail.prev
        if node is not None:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.Nodes = {} #key: node
        self.NodeData = defaultdict(DoublyLinkedList)
        self.minfreq = 0

    def update(self, node):
        freq = node.freq
        dll = self.NodeData[freq]
        dll.pop(node)
        if self.minfreq == freq and self.NodeData[freq].size == 0:
            self.minfreq += 1
        newdll = self.NodeData[freq + 1]
        newdll.append(node)
        node.freq += 1

    def get(self, key: int) -> int:
        if key not in self.Nodes:
            return -1
        node = self.Nodes[key]
        self.update(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return -1
        
        if key in self.Nodes:
            node = self.Nodes[key]
            node.val = value
            self.update(node)
        else:
            if self.size == self.capacity:
                node = self.NodeData[self.minfreq].pop()
                del self.Nodes[node.key]
                self.size -= 1
            node = Node(key, value)
            self.Nodes[key] = node
            self.NodeData[1].append(node)
            self.size += 1
            self.minfreq = 1


'''
 todo:
check minfreq initial value
check in case of delete of dll, how it is check if no element is present there
'''        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
