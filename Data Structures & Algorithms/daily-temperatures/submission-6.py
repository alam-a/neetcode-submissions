class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        stack.append(0)
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res