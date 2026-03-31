class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True

        def break_down(n: int) -> int:
            res = 0
            while n:
                res += (n % 10)**2
                n //= 10
            return res
        res = set()
        while n not in res:
            res.add(n)
            if n == 1:
                return True
            n = break_down(n)
        return False