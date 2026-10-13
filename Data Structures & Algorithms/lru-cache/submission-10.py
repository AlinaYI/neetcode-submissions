class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {} # key: node
        self.capacity = capacity
        self.size = 0

    def delNode(self, node):
        nodeF = node.prev
        nodeB = node.next

        nodeF.next = nodeB
        nodeB.prev = nodeF

        del self.hashmap[node.key]
        self.size -= 1

    def addFront(self, node):
        
        currFirst = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = currFirst
        currFirst.prev = node

        self.hashmap[node.key] = node
        self.size += 1
        if self.size > self.capacity:
            self.delNode(self.tail.prev)


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.delNode(node)
        self.addFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delNode( self.hashmap[key] )
        node = Node(key, value)
        self.addFront(node)
