class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.hashmap = {} # key:node
        self.size = 0
        self.capacity = capacity

    def addFront(self, node):
        
        curr_first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = curr_first
        curr_first.prev = node

        self.size += 1
        if self.size > self.capacity:
            self.removeNode(self.tail.prev)
        
        self.hashmap[node.key] = node
 
    def removeNode(self, node):
        key = node.key
        if key not in self.hashmap:
            return False
        
        node_pre = node.prev
        node_next = node.next

        node_pre.next = node_next
        node_next.prev = node_pre

        del self.hashmap[key]
        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.removeNode(node)
        self.addFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.removeNode(self.hashmap[key])
        
        newNode = ListNode(key, value)
        self.addFront(newNode)
