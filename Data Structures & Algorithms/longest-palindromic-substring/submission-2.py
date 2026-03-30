class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        max_len = 1
        res = s[0]
        for i in range(L):
            l, r = i-1, i+1
            while l >= 0 and r < L and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < L and s[l] == s[r]:
                if r-l+1 > max_len:
                    max_len = r-l+1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
        return res