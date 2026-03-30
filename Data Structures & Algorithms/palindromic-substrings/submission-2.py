class Solution:
    def countSubstrings(self, s: str) -> int:
        def count_palindrome(i, j):
            count = 0
            while 0 <= i < len(s) and 0 <= j < len(s) and s[i] == s[j]:
                count += 1
                i-=1
                j+=1
            return count
        res = 0
        for i in range(len(s)):
            res += count_palindrome(i, i)
            res += count_palindrome(i, i+1)
        return res