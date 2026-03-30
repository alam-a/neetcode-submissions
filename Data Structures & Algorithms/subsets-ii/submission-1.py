class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        self.res = set()
        def dfs(sub, index):
            self.res.add(tuple(sorted(sub)))
            for i in range(index, L):
                dfs(sub+[nums[i]], i+1)
        dfs([], 0)
        return [list(s) for s in self.res]