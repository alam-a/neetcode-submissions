class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        path = []
        res = []
        def dfs(n):
            if n == len(digits):
                return res.append("".join(path))
            for c in mappings[digits[n]]:
                path.append(c)
                dfs(n+1)
                path.pop()
        dfs(0)
        return res