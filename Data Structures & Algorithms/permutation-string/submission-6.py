class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq_list = [0] * 26
        s2_freq_list = [0] * 26
        for i in range(len(s1)):
            s1_freq_list[ord(s1[i]) - ord('a')] += 1
            s2_freq_list[ord(s2[i]) - ord('a')] += 1
        
        l, r = 0, len(s1)
        while r < len(s2):
            if s1_freq_list == s2_freq_list:
                return True
            
            s2_freq_list[ord(s2[l]) - ord('a')] -= 1
            s2_freq_list[ord(s2[r]) - ord('a')] += 1
            l += 1
            r += 1
        return s1_freq_list == s2_freq_list