class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        
        # build double linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.dict = {}
        self.capacity = capacity
        self.size = 0

    def addFront(self, node):

        curr_first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = curr_first
        curr_first.prev = node

        self.size += 1
        self.dict[node.key] = node
        if self.size > self.capacity:
            self.remove(self.tail.prev)

    def remove(self, node):

        node_prev = node.prev
        node_next = node.next

        node_prev.next = node_next
        node_next.prev = node_prev

        self.dict.pop(node.key)
        self.size -= 1

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        node = self.dict[key]
        self.remove(node)
        self.addFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])

        newnode = Node(key, value)
        self.addFront(newnode)
