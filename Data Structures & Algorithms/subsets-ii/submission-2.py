class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def dfs(index: int):
            res.append(path[:])
            for i in range(index, len(nums)):
                if i > index and nums[i-1] == nums[i]:
                    continue
                path.append(nums[i])
                dfs(i+1)
                path.pop()
        dfs(0)
        return res