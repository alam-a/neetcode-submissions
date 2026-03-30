class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        l, r, cc = 0, 0, 0
        while l < len(s2) - len(s1) + 1:
            print(freq, l, r)
            if r >= len(s2):
                return False
            
            if s2[r] in freq:
                if freq[s2[r]] == 0:
                    while s2[l] != s2[r]:
                        freq[s2[l]] += 1
                        l += 1
                        cc -= 1
                    l += 1
                else:
                    freq[s2[r]] -= 1
                    cc += 1
            else:
                while l <= r:
                    if s2[l] in freq:
                        freq[s2[l]] += 1
                        cc -= 1
                    l += 1
            r += 1
            if cc == len(s1):
                return True
        return False