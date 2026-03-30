class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # from collections import deque
        stack = []
        res = []
        def backtrack(un):
            if len(stack) == 2*n:
                if not un:
                    res.append("".join(stack))
                return
            for p in ["(", ")"]:
                stack.append(p)
                if p == "(":
                    backtrack(un+1)
                elif un > 0:
                    backtrack(un-1)
                stack.pop()
        backtrack(0)
        return res