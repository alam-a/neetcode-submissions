class Deque:
    def __init__(self, key:int, val: int, left: Deque = None, right: Deque = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
    
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Deque(-1, -1)
        self.tail = Deque(-2, -1)
        self.head.right = self.tail
        self.tail.left = self.head
        self.elems = {} #stores refernce to Deque node
        self.capacity = capacity

    def get(self, key: int) -> int:
        print(key)
        if key in self.elems:
            node = self.elems[key]
            if node != self.head:
                temp = node
                node.left.right = node.right
                if node.right:
                    node.right.left = node.left
                temp.left = None
                temp.right = self.head
                self.head.left = temp
                self.head = temp
                self.print_lru()
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        print(key, value)#, self.head.key, self.head.val, self.tail.key, self.tail.val)
        if key in self.elems:
            return
        node = Deque(key = key, val = value, right = self.head)
        self.head.left = node
        self.head = node
        self.elems[key] = node
        if len(self.elems) > self.capacity:
            while self.tail.val < 0:
                self.tail = self.tail.left
                self.tail.right = None
            #evict oldest
            # delete dict entry
            if self.tail.key in self.elems:
                del self.elems[self.tail.key]
            #delete the tail node i.e. the least recently used node
            print(f"deleting: {self.tail.key}, {self.tail.val}")
            left = self.tail.left
            left.right = None
            self.tail = left
        self.print_lru()

    def print_lru(self):
        tmp = self.head
        while tmp:
            print(f"({tmp.key}, {tmp.val}) --> ", end = "")
            tmp = tmp.right
        print()

        tmp = self.tail
        while tmp:
            print(f"({tmp.key}, {tmp.val}) --> ", end = "")
            tmp = tmp.left
        print()

        for k, v in self.elems.items():
            print(f"[{k}: ({v.key}, {v.val})]", end="\t")
        print()