class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, path = [], []
        def dfs(index: int, acc: int):
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if acc + candidates[i] == target:
                    res.append(path[:])
                    res[-1].append(candidates[i])
                if acc + candidates[i] >= target:
                    break
                path.append(candidates[i])
                dfs(i + 1, acc + candidates[i])
                path.pop()
        dfs(0, 0)
        return res