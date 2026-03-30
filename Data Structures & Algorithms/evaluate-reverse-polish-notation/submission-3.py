import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(l, r, o):
            if o == "+":
                return l + r
            elif o == "-":
                return l-r
            elif o == "*":
                return l*r
            else:
                res = l/r
                if res > 0:
                    return math.floor(res)
                return math.ceil(res)

        operands = {"+", "-", "*", "/"}
        from collections import deque
        stack = deque()
        for t in tokens:
            if t in operands:
                right = stack.pop()
                left = stack.pop()
                stack.append(operate(left, right, t))
            else:
                stack.append(int(t))
        return stack.pop()

