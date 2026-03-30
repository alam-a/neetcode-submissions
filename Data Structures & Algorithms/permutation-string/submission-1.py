class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for c in s1:
            freq[c] = freq.get(c, 0) + 1
        
        # l = start of the pattern detected
        # r = current position in s2
        l, r = 0, 0
        while r < len(s2):
            c = s2[r]
            # if the current char matches and is available in freq, decrement that
            if c in freq and freq[c] > 0:
                freq[c] -= 1
            # if the current char matches but not available in freq, that means we
            # have too many of the current char in the pattern, so we start pruning
            # from the start of the pattern till the current char is found, then we 
            # prune one instance of the current char as well, at the same time we keep
            # increasing the value of l
            elif c in freq and freq[c] == 0:
                while s2[l] != c:
                    freq[s2[l]] += 1
                    l += 1
                # After the loop, s2[l] == c. We don't increment freq[c] just to decrement it again.
                # Instead, we just move the left pointer past the first occurrence of 'c'.
                l += 1
            # if the current char does not match, then we move the l pointer to r
            # one by one, incrementing the freq if the char at l position is found
            # in s2
            else:
                while l < r:
                    if s2[l] in freq:
                        freq[s2[l]] += 1
                    l += 1
                l = r + 1
            # if the pattern is matched, then pointer  r - l + 1 should equal length
            # of the original string
            if r - l + 1 == len(s1):
                return True
            r += 1
        return False