class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev, prev_prev = nums[1], nums[0]
        for i in range(2, len(nums)):
            num = nums[i]
            temp = prev_prev
            prev_prev = max(prev, prev_prev)
            prev = temp + num
            print(prev, prev_prev)

        return max(prev, prev_prev)