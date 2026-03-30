class Node:
    def __init__(self, key:int, val: int, next: Node = None, prev: Node = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1, None, self.head)
        self.head.next = self.tail
        self.elems = {}

    def get(self, key: int) -> int:
        if key in self.elems:
            temp = self.elems[key]
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = self.head.next
            self.head.next = temp
            temp.prev = self.head
            temp.next.prev = temp
            return temp.val
        return -1

    def put(self, key: int, value: int) -> None:
        print(key, value, self.head.next.val, self.tail.prev.val)
        if key in self.elems:
            temp = self.elems[key]
            temp.val = value
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.next = self.head.next
            self.head.next.prev = temp
            self.head.next = temp
            temp.prev = self.head
        elif len(self.elems) == self.capacity:
            d = self.tail.prev
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev
            del self.elems[d.key]

            temp = Node(key, value, self.head.next, self.head)
            self.head.next.prev = temp
            self.head.next = temp
            self.elems[key] = temp
        else:
            temp = Node(key, value, self.head.next, self.head)
            self.head.next.prev = temp
            self.head.next = temp
            self.elems[key] = temp