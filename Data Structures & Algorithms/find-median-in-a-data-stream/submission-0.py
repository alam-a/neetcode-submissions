from heapq import heappush_max, heappop_max

class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        heappush_max(self.arr, num)

    def findMedian(self) -> float:
        if len(self.arr) == 1:
            return self.arr[0]
        # elif len(self.arr) == 2:
        #     return sum(self.arr) / 2
        temp = self.arr[:]
        L = len(self.arr)
        if len(self.arr) % 2 == 0:
            for _ in range(L // 2 - 1):
                heappop_max(self.arr)
            n1, n2 = heappop_max(self.arr), heappop_max(self.arr)
            self.arr = temp
            return (n1 + n2) / 2
        else:
            for _ in range(L // 2):
                heappop_max(self.arr)
            n1 = heappop_max(self.arr)
            self.arr = temp
            return n1
