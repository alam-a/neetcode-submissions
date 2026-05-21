class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [""] * (len(word1) + len(word2))
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        i = 0
        for c1, c2 in zip(word1, word2):
            res[i] = c1
            res[i+1] = c2
            i = i + 2

        return "".join(res) + word1[len(word2):]