class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(index: int):
            if index > len(nums):
                return
            res.append(path[:])
            for i in range(index, len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return res
        