class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, index):
            res.append(curr[:])
            for i in range(index, len(nums)):
                curr.append(nums[i])
                dfs(curr, i + 1)
                curr.pop()
        dfs([], 0)
        return res