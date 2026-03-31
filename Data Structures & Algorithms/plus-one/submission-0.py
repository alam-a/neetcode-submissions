class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for digit in digits[::-1]:
            num = digit + carry
            if num > 9:
                res.append(num % 10)
                carry = num // 10
            else:
                res.append(num)
                carry = 0
        res.append(carry) if carry else None
        return res[::-1]