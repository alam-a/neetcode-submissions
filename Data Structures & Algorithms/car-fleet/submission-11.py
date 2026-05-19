class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = list(map(lambda p_s: (target - p_s[0]) / p_s[1], sorted(zip(position, speed))))
        res = 1
        prev = times[-1]
        for curr in times[::-1]:
            if curr > prev:
                res += 1
                prev = curr
        return res