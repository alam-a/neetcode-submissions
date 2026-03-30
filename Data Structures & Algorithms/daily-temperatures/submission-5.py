class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = collections.deque()
        res = [0 for _ in temperatures]
        stack.append((temperatures[0], 0))

        for i, temp in enumerate(temperatures[1:], 1):
            while stack and stack[-1][0] < temp:
                res[stack.pop()[1]] = i - stack[-1][1]
            stack.append((temp, i))
        return res