class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        res, longest = 0, ""
        n = 0
        for index in range(L):
            l, r, temp = index - 1, index + 1, 1
            while l >= 0 and r < L and s[l] == s[r]:
                l -= 1
                r += 1
                temp += 2
            if temp > res:
                res = temp
                longest = s[l+1: r]

        for index in range(L):
            l, r, temp = index, index + 1, 0
            while l >= 0 and r < L and s[l] == s[r]:
                l -= 1
                r += 1
                temp += 2
            if temp > res:
                res = temp
                longest = s[l+1: r]
        return longest
