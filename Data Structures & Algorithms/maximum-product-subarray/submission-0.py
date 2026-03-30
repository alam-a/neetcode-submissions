class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Not a dp solution
        res = -1e9
        for i in range(len(nums)):
            curr = nums[i]
            res = max(res, curr)
            for j in range(i+1, len(nums)):
                curr *= nums[j]
                res = max(res, curr)
        return res