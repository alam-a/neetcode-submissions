class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(sub: List[int]):
            if not sub:
                res.append(path[:])
                return
            for i in range(len(sub)):
                path.append(sub[i])
                dfs(sub[0:i] + sub[i+1:])
                path.pop()
        dfs(nums)
        return res