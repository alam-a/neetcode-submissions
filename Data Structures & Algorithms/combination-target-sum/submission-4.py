class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(index: int, acc: int) -> None:
            if acc == target:
                res.append(path[:])
            for i in range(index, len(nums)):
                if acc + nums[i] > target:
                    continue
                path.append(nums[i])
                dfs(i, acc + nums[i])
                path.pop()
        dfs(0, 0)
        return res
