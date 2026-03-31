class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1, L2 = len(s1), len(s2)
        if L1 > L2:
            return False
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        for i in range(L1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            s2_freq[ord(s2[i]) - ord('a')] += 1
        
        l, r, is_perm = 0, L1 - 1, s1_freq == s2_freq
        while not is_perm and r < L2 - 1:
            s2_freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            s2_freq[ord(s2[r]) - ord('a')] += 1
            is_perm = s1_freq == s2_freq
        return is_perm