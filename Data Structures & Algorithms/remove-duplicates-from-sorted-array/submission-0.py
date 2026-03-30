class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        k = 1
        for num in nums[1:]:
            if num == prev:
                nums.pop(k)
                continue
            prev = num
            k += 1
        return len(nums)