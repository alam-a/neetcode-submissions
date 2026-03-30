class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        reference, counter = {}, {}
        for c in s1:
            reference[c] = reference.get(c, 0) + 1
        counter = {k: 0 for k in reference}

        l, r = 0, 0
        while r < len(s2):
            rc = s2[r]
            if rc in reference:
                while counter[rc] == reference[rc]:
                    counter[s2[l]] -= 1
                    l += 1
                counter[rc] += 1
                if counter == reference:
                    return True
            else:
                counter = {k: 0 for k in reference}
                l = r + 1
            r += 1
        return False 
