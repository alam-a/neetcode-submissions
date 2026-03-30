class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        last, slast = 2, 1
        for i in range(2, n):
            temp = last
            last += slast
            slast = temp
        return last
