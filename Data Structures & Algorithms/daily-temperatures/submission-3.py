class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dbw = [0 for _ in temperatures]
        from collections import deque
        q = deque()
        q.append((temperatures[0], 0))
        for index in range(1, len(temperatures)):
            while q and temperatures[index] > q[-1][0]:
                tt, ti = q.pop()
                dbw[ti] = index - ti
            q.append((temperatures[index], index))
        return dbw