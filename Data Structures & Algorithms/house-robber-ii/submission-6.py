class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        def rob_from_index(nums):
            if len(nums) == 1:
                return nums[0]
            slast = nums[0]
            last = max(nums[1], slast)
            for num in nums[2:]:
                temp = last
                last = max(slast+num, last)
                slast = temp
            return last
        return max(rob_from_index(nums[:-1]), rob_from_index(nums[1:]))