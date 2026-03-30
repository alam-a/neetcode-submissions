class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        def check(i, j):
            if i > j:
                return True
            if not s[i].isalnum():
                return check(i+1, j)
            elif not s[j].isalnum():
                return check(i, j-1)
            elif s[i] == s[j]:
                return check(i+1, j-1)
            return False
        return check(0, len(s)-1)
        