class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = len(s)
        l, r = 0, L - 1
        while l < r:
            while l < L and not s[l].isalnum():
                l += 1
            while r >= 0 and not s[r].isalnum():
                r -= 1
            if l < r and s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True