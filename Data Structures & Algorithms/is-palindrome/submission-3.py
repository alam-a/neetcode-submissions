class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join([c for c in s.lower() if ord('a') <= ord(c) <= ord('z')])
        return ns[::-1] == ns