class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        for c1, c2 in zip(word1, word2):
            res.append(c1)
            res.append(c2)
        
        res = "".join(res)
        if len(word1) > len(word2):
            return res + word1[len(word2):]
        elif len(word1) < len(word2): 
            return res + word2[len(word1):]
        else:
            return res