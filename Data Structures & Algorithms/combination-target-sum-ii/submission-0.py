class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        path = []

        def dfs(start: int, sumn: int) -> None:
            if sumn == target:
                res.add(tuple(path))
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                sumn += path[-1]
                dfs(i+1, sumn)
                sumn -= path[-1]
                path.pop()
        dfs(0, 0)
        return [list(path) for path in res]