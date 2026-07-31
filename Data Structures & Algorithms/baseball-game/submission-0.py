class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        stack.append(0)
        prev_prev, prev = 0, 0
        for op in operations:
            if op == '+':
                stack.append(prev + prev_prev)
            elif op == 'D':
                stack.append(2 * stack[-1])
            elif op == 'C':
                stack.pop()
            else:
                prev_prev = stack[-1]
                prev = int(op)
                stack.append(prev)
        print(stack)
        return sum(stack)