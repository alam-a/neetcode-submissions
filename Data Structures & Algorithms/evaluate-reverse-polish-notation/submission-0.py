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
                return l/r

        operands = {"+", "-", "*", "/"}
        from collections import deque
        stack = deque()
        for t in tokens:
            if t in operands:
                right = int(stack.pop())
                left = int(stack.pop())
                stack.append(int(operate(left, right, t)))
            else:
                stack.append(t)
        return stack.pop()

