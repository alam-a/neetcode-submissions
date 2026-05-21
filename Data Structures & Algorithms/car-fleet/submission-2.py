class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [p/s for p, s in sorted(zip(map(lambda x: target - x, position), speed))]
        print(time)
        l, c = float("inf"), 0
        for t in time:
            if t >= l:
                c+=1
            l = t
        return c