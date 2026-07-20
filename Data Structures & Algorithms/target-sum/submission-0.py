class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            if not target:
                return 1
            else:
                return 0
        res = (
            self.findTargetSumWays(nums[1:], target + nums[0]) 
            + self.findTargetSumWays(nums[1:], target - nums[0])
        )
        return res