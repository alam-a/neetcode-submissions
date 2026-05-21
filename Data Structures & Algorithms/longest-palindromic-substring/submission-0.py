class Solution:
    def longestPalindrome(self, s: str) -> str:
        l, L = 0, len(s)
        res_i, res_j = 0, 0
        while l < L:
            r = L-1
            while l < r:
                if s[l] != s[r]:
                    r-=1
                    continue
                i, j = l, r
                print(i, j)
                while l < r and s[l] == s[r]:
                    l+=1
                    r-=1
                if r <= l and res_j-res_i < j-i:
                    res_i = i
                    res_j = j
                l = i
            l+=1
        return s[res_i: res_j+1]