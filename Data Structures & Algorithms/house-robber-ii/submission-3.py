class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def check_part(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            res = [0 for _ in nums]
            res[0], res[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, len(nums)):
                res[i] = max(res[i-2]+nums[i], res[i-1])
            return res[-1]
        l = check_part(nums[:-1])
        r = check_part(nums[1:])

        return max(l, r)