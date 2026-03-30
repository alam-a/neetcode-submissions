class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        def dfs(sub, pos):
            if tuple(sub) not in self.res:
                self.res.add(tuple(sub))
            for i in range(pos, len(nums)):
                dfs(sub+[nums[i]], i+1)
        dfs([], 0)
        return [list(s) for s in self.res]