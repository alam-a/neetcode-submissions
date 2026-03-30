class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [p/s for p, s in sorted(zip(map(lambda x: target-x, position), speed))]
        l, c = time[0], 1
        for t in time[1:]:
            if t > l:
                c += 1
                l = t
        return c