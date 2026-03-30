class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        self.res = set()
        self.ref = {}
        self.visited = {}
        for num in nums:
            self.visited[num] = 0
            self.ref[num] = 1 + self.ref.get(num, 0)

        def dfs(sub, index):
            self.res.add(tuple(sorted(sub)))
            for i in range(index, L):
                if self.visited[nums[i]] == self.ref[nums[i]]:
                    continue
                self.visited[nums[i]] += 1
                dfs(sub+[nums[i]], i+1)
                self.visited[nums[i]] -= 1
        dfs([], 0)
        return [list(s) for s in self.res]