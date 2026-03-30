class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        #brute force
        i, curr = 0, ""
        while i < len(strs[0]):
            c = strs[0][i]
            for s in strs:
                if i >= len(s) or c != s[i]:
                    return curr
            curr = strs[0][:i+1]
            i+=1
        return curr

        