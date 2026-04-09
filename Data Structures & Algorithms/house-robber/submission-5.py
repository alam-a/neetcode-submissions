class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        prev, prev_prev = max(nums[0], nums[1]), nums[0]
        for num in nums[2:]:
            prev_prev, prev = prev, max(prev_prev + num, prev)
        return prev