'''
[nums1, nums2] ==> [nums2, nums1]

hashmap --> get O1, {key:node}
put --> hashmap

linked-list , nums1 <--> nums2
'''

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # self.head --> self.tail
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # {key:node}
        self.hashmap = {}
        self.size = 0
        self.capacity = capacity

    def add_front(self, node):
        # head -> curr_fisrt
        curr_fisrt = self.head.next

        # head -> node
        self.head.next = node
        # head <-> node
        node.prev = self.head

        # head <-> node -> curr_first
        node.next = curr_fisrt
        # head <-> node <-> curr_first
        curr_fisrt.prev = node

        self.hashmap[node.key] = node
        self.size += 1
        if self.size > self.capacity:
            self.delete_node(self.tail.prev)

    def delete_node(self, node):
        # node1 <-> node <-> node2

        node_prev = node.prev # node1
        node_next = node.next # node2

        # node1  -> node2
        node_prev.next = node_next
        # node1  <-> node2
        node_next.prev = node_prev

        del self.hashmap[node.key]
        self.size -= 1

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
        print(f"hashmap: {self.hashmap}")
