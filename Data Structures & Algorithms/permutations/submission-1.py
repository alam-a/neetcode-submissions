class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(nums: List[int]) -> None:
            if not nums:
                res.append(path[:])
            for i in range(len(nums)):
                path.append(nums[i])
                dfs(nums[:i] + nums[i+1:])
                path.pop()
        dfs(nums)
        return res