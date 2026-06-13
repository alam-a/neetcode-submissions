class MyStack:

    def __init__(self):
        self.active = deque()
        self.passive = deque()

    def push(self, x: int) -> None:
        self.active.append(x)

    def pop(self) -> int:
        t = None
        while self.active:
            t = self.active.popleft()
            if self.active:
                self.passive.append(t)
        self.active, self.passive = self.passive, self.active
        return t

    def top(self) -> int:
        return self.active[-1]

    def empty(self) -> bool:
        return len(self.active) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()