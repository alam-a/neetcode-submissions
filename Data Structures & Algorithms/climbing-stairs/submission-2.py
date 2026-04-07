from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        prev, prev_prev = 2, 1
        for i in range(3, n):
            prev, prev_prev = prev + prev_prev, prev
        return prev + prev_prev