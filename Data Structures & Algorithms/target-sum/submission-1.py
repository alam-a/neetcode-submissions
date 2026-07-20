from functools import cache
class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        L = len(nums)
        @cache
        def dfs(index, target):
            if index == L:
                if not target:
                    return 1
                else:
                    return 0
            res = (
                dfs(index+1, target + nums[index]) 
                + dfs(index+1, target - nums[index])
            )
            return res
        return dfs(0, target)