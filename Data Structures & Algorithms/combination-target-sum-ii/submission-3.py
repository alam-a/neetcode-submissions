class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        path = []
        def dfs(start: int, rem: int) -> None:
            if rem == 0:
                res.add(tuple(path))
                return
            
            if rem < 0 or start == len(candidates):
                return
            num = candidates[start]
            path.append(num)
            dfs(start+1, rem-num)
            path.pop()
            dfs(start+1, rem)
        dfs(0, target)
        return [list(path) for path in res]