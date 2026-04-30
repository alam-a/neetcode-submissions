class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def dfs(rem: List[int]):
            if len(rem) == 0:
                res.append(path[:])
                return
            for i in range(len(rem)):
                path.append(rem[i])
                dfs(rem[:i]+rem[i+1:])
                path.pop()
        dfs(nums)
        return res