class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        q, res = deque(), [0 for _ in temperatures]
        q.append((temperatures[0], 0))

        for i, temp in enumerate(temperatures[1:], 1):
            # print(q)
            while q and q[-1][0] < temp:
                res[q[-1][1]] = i - q[-1][1]
                q.pop()
            q.append((temp, i))
        
        return res