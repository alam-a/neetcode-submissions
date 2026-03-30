class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        max_len = 1
        res = s[0]
        for i in range(L-1):
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    res = s[l:r+1]
                    max_len = r-l+1
                l-=1
                r+=1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > max_len:
                    res = s[l:r+1]
                    max_len = r-l+1
                l-=1
                r+=1

        return res