class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        res = []
        curr = []
        def dfs(nums: List[int]):
            if len(curr) == L:
                res.append(curr[:])
                return
            for i, num in enumerate(nums):
                curr.append(num)
                dfs(nums[:i] + nums[i+1:])
                curr.pop()
        dfs(nums)
        return res