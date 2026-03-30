class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l2 < l1:
            return False
        freq_s1, freq_s2 = [0] * 26, [0] * 26
        for i in range(l1):
            freq_s1[ord(s1[i]) - ord('a')] += 1 
            freq_s2[ord(s2[i]) - ord('a')] += 1
        if freq_s1 == freq_s2:
            return True

        l, r = 0, l1 - 1
        while r+1 < l2:
            freq_s2[ord(s2[l]) - ord('a')] -= 1 
            freq_s2[ord(s2[r+1]) - ord('a')] += 1
            if freq_s1 == freq_s2:
                return True
            l += 1
            r += 1
        return False