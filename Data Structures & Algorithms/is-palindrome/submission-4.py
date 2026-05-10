class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = "".join([c for c in s.lower() if ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')])
        return ns[::-1] == ns