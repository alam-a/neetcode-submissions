class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        elif n in self.memo:
            return self.memo[n]
        else:
            self.memo[n-2] = self.climbStairs(n-2)
            self.memo[n-1] = self.climbStairs(n-1)
        return self.memo[n-1] + self.memo[n-2]