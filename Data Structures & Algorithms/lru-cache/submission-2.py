class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.prev, self.tail.next = self.tail, self.head
        self.cache = {}
        self.capacity = capacity
    def print_lru(self):
        temp = self.head
        while temp:
            print(temp.key, temp.val, end=" -> ")
            temp = temp.prev
        print()

    def get(self, key: int) -> int:
        # print("get")
        # self.print_lru()
        if key in self.cache:
            node = self.cache[key]
            self.remove_node(node)
            self.add_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # print("put")
        # self.print_lru()
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove_node(node)
            self.add_to_head(node)
            return
        if len(self.cache) == self.capacity:
            self.delete_last()
        node = Node(key, value)
        self.add_to_head(node)
        self.cache[key] = node
    
    def remove_node(self, node: Node) -> None:
        node.next.prev, node.prev.next = node.prev, node.next
        node.next, node.prev = None, None
    
    def delete_last(self) -> None:
        node = self.tail.next
        self.tail.next.next.prev, self.tail.next = self.tail, self.tail.next.next
        # print(node)
        del self.cache[node.key]
    
    def add_to_head(self, node: Node) -> None:
        prev = self.head.prev
        node.next, node.prev = self.head, prev
        prev.next = self.head.prev = node



