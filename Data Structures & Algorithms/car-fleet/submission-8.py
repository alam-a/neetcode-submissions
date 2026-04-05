class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = list(map(lambda p_s: (target - p_s[0]) / p_s[1], sorted(zip(position, speed), reverse=True)))

        last, res = time[0], 1
        for t in time[1:]:
            if last < t:
                last = t
                res += 1
        return res