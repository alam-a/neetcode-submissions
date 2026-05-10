class MinStack:

    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        minimum = val if not self.q else min(self.q[-1][1], val)
        self.q.append((val, minimum))
        
    def pop(self) -> None:
        self.q.pop()

    def top(self) -> Optional[int]:
        return self.q[-1][0] if self.q else None

    def getMin(self) -> Optional[int]:
        return self.q[-1][1] if self.q else None