class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack = deque()
        pmap = {"]": "[", "}": "{", ")": "("}

        for i in range(len(s)):
            if s[i] in pmap:
                print(s[i])
                if len(stack) <= 0:
                    return False
                elif pmap[s[i]] != stack.pop():
                    return False
            else:
                stack.append(s[i])
            print(s[i], stack)
        return False if len(stack) > 0 else True
                
                



