class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num_str: str) -> int:
            res = 0
            for c in num_str[::-1]:
                res *= 10
                res += (ord(c) - ord('0'))
            return res
        return f"{convert(num1) * convert(num2)}"