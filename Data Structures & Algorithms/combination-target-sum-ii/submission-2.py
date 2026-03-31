class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def dfs(start: int, sumn: int) -> None:
            if sumn == target:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if i > start and candidate == candidates[i-1]:
                    continue
                prev = candidate

                if sumn + candidate > target:
                    break
                path.append(candidate)
                dfs(i+1, sumn + candidate)
                path.pop()
        dfs(0, 0)
        return res
