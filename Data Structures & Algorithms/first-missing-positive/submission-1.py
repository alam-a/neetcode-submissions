class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            ni = abs(nums[i])
            if nums[i] != 0 and ni <= len(nums):
                ni = ni - 1
                if nums[ni] > 0:
                    nums[ni] *= -1
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1