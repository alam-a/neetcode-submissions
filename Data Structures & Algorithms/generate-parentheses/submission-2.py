class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        L = 2 * n
        res = []
        path = []
        def dfs(imf: int): # imf: imbalance number
            if len(path) == L:
                if imf == 0:
                    res.append("".join(path))
                return
            if len(path) > n and imf >= n:
                return

            if imf > 0 :
                path.append(")")
                dfs(imf-1)
                path.pop()
            path.append("(")
            dfs(imf+1)
            path.pop()
        dfs(0)
        return res