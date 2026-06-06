class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num_str: str) -> int:
            res = 0
            for c in num_str:
                res *= 10
                res += (ord(c) - ord('0'))
            return res
        num1: int = convert(num1)
        num2: int = convert(num2)
        return f"{num1 * num2}"