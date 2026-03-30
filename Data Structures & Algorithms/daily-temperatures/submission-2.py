class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        stack = deque()
        dbw = [0 for _ in temperatures]
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tt, it = stack.pop()
                dbw[it] = i - it
            stack.append((temp, i))
        return dbw