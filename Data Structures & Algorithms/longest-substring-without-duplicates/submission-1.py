class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, pos, curr, maximum = 0, {}, 0, 0
        
        l = 0
        visited = set()
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[r])
            maximum = max(r-l+1, maximum) 
        return maximum