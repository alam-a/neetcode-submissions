class Solution:
    def findMin(self, nums: List[int]) -> int:
        prev = nums[0]
        for num in nums[1:]:
            if num < prev:
                return num
        return prev
        