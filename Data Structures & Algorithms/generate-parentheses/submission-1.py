class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(extra_open: int) -> None:
            # op means open (
            if extra_open == 0 and len(path) == 2 * n:
                res.append("".join(path))
                return
            if len(path) > 2 * n:
                return
            if extra_open:
                path.append(')')
                dfs(extra_open-1)
                path.pop()
            path.append('(')
            dfs(extra_open + 1)
            path.pop()
        dfs(0)
        return res