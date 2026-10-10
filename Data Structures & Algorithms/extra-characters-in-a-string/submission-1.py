class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = [[] for _ in range(26)]
        for word in dictionary:
            words[ord(word[0]) - ord('a')].append(word)
        # print(words)
        self.res = 50
        def dfs(i, e):
            if i == len(s):
                self.res = min(self.res, e)
                return
            found = False
            for word in words[ord(s[i]) - ord('a')]:
                if len(word) <= len(s) - i:
                    # print(word, s[i: i + len(word)])
                    if word == s[i:i+len(word)]:
                        found = True
                        dfs(i+ len(word), e)
            dfs(i+1, e+1)
        dfs(0, 0)
        return self.res