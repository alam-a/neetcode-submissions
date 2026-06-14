class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                pi, pt = stack.pop()
                res[pi] = i - pi
            stack.append((i, temperature))
        return res