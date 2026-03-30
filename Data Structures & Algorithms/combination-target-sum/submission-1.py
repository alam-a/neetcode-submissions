class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = {num: 0 for num in nums}
        res = set()
        def dfs(curr):
            if curr == target:
                t = []
                for k, v in path.items():
                    for i in range(v):
                        t.append(k)
                res.add(tuple(t))
            if curr > target:
                return None
            for num in nums:
                path[num] += 1
                dfs(curr+num)
                path[num] -= 1
        dfs(0)
        return [list(i) for i in res]
        