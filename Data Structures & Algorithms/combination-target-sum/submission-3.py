class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def dfs(start: int, rem: int) -> None:
            if rem == 0:
                res.append(path[:])
                return
            if rem < 0 or start == len(nums):
                return

            num = nums[start]    
            path.append(num)
            rem -= num
            dfs(start, rem)
            rem += num
            path.pop()

            dfs(start+1, rem)
        dfs(0, target)
        return res