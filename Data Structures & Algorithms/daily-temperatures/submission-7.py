class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ms = collections.deque() # monotonically decreasing stack
        ms.append((temperatures[0], 0))
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures[1:], 1):
            while ms and temperature > ms[-1][0]:
                high, pos = ms.pop()
                res[pos] = i - pos
            ms.append((temperature, i))
        return res