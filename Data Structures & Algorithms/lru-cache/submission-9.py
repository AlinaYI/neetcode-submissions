class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {} # node.key : node
        self.size = 0
        self.capacity = capacity

    def addNode(self, node):
        currFirst = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = currFirst
        currFirst.prev = node
        self.size += 1
        self.hashmap[node.key] = node

        if self.size > self.capacity:
            self.delNode(self.tail.prev)

    def delNode(self, node):
        nodeP = node.prev
        nodeN = node.next
        
        nodeP.next = nodeN
        nodeN.prev = nodeP
        self.size -= 1
        del self.hashmap[node.key]

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.delNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashmap:
            self.delNode(self.hashmap[key])
        newNode = ListNode(key, value)
        self.addNode(newNode)
