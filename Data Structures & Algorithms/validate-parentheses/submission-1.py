class Solution:
    def isValid(self, s: str) -> bool:
        partner = {")": "(", "]": "[", "}": "{"}
        from collections import deque
        stack = deque()

        for c in s:
            if c in partner:
                if len(stack)==0 or partner[c] != stack.pop():
                    return False
                continue
            stack.append(c)
        
        return True if len(stack) == 0 else False

