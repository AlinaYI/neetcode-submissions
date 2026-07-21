class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

        # {key: node}
        self.hashmap = {}
        self.capacity = capacity
        self.size = 0
    
    def add_front(self, node):
        curr_first = self.head.next
        self.head.next = node
        node.prev = self.head

        node.next = curr_first
        curr_first.prev = node

        self.hashmap[node.key] = node
        self.size += 1
        if self.size > self.capacity:
            self.delete_node(self.tail.prev)
        
    def delete_node(self, node):
        node_prev = node.prev
        node_next = node.next
        
        node_prev.next = node_next
        node_next.prev = node_prev

        self.size -= 1
        del self.hashmap[node.key]

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]
        self.delete_node(node)
        self.add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.delete_node(self.hashmap[key])
        node = Node(key, value)
        self.add_front(node)

