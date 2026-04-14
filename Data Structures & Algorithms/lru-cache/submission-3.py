class Node:
    def __init__(self, key: int, val: int, prev: Node = None, next: Node = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.tail, self.head = Node(-1, -1), Node(-1, -1)
        self.tail.next, self.head.prev = self.head, self.tail

    def get(self, key: int) -> int:
        print("get")
        if key in self.cache:
            node = self.cache[key]
            self.detach_neighbors(node)
            self.add_to_head(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        print("put")
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.detach_neighbors(node)
            self.add_to_head(node)
        else:
            node = Node(key, value)
            self.add_to_head(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                self.evict_last()

    def detach_neighbors(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def add_to_head(self, node: Node) -> None:
        node.prev, node.next = self.head.prev, self.head
        self.head.prev.next, self.head.prev = node, node
    
    def evict_last(self) -> None:
        temp = self.tail.next
        temp.next.prev, temp.prev.next = self.tail, temp.next
        del self.cache[temp.key]
        del temp
