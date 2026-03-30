class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        slast = nums[0]
        last = max(slast, nums[1])
        for num in nums[2:]:
            temp = last
            last = max(last, slast+num)
            slast = temp
        return last