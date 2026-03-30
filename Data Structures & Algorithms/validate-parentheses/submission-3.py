class Solution:
    def isValid(self, s: str) -> bool:
        complement = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in complement:
                if not stack:
                    return False
                elif stack[-1] != complement[c]:
                    return False 
                else:
                    stack.pop()
            else:
                stack.append(c)
        return stack == []