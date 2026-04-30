class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        res = [1 for _ in nums]
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * acc
            acc *= nums[i]
        return res