from functools import cache
class Solution:
    
    @cache
    def tribonacci(self, n: int) -> int:
        if n in (1, 2):
            return 1
        if n < 1:
            return 0
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)