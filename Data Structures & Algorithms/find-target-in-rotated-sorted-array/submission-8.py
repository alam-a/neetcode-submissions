class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_min_index(nums)
        if nums[0] <= target <= nums[min_index]:
            return self.binary_search(nums, 0, min_index, target)
        else:
            return self.binary_search(nums, min_index+1, len(nums)-1, target)

    def binary_search(self, nums, l, r, target):
        while l < r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                l = mid+1
            else:
                r = mid-1
        return -1
           
    def find_min_index(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = l
        return l