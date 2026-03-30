class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_map = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y if x / y > 0 else math.ceil(x/y),
        }
        for token in tokens:
            if token in operator_map:
                print(stack, token)
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(operator_map[token](op1, op2))
            else:
                stack.append(int(token))
        return stack[0]
