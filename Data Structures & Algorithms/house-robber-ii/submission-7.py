class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        #start from 0
        curr, prev = max(nums[0], nums[1]), nums[0]
        for i in range(2, len(nums) - 1):
            curr, prev = max(prev + nums[i], curr), curr
        res = curr
 
        #start from 1
        curr, prev = max(nums[1], nums[2]), nums[1]
        for i in range(3, len(nums)):
            curr, prev = max(prev + nums[i], curr), curr
        res = max(res, curr)
        return res