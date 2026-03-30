class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        stack = deque()
        stack.append((temperatures[-1], len(temperatures)-1))
        dbw = [0 for _ in range(len(temperatures))] #days_before_warmer

        for i in range(len(temperatures) - 2, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]: 
                top, ti = stack.pop()
                if stack and top != stack[-1][0]:
                    dbw[ti] = stack[-1][1] - ti
            stack.append((temperatures[i], i))
        
        while stack:
            temp, i = stack.pop()
            if stack:
                dbw[i] = stack[-1][1] - i
        return dbw