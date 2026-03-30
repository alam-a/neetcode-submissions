class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if pivot == 0:
            return self.bin_search(nums, 0, len(nums)-1, target)
        elif nums[0] <= target <= nums[pivot-1]:
            return self.bin_search(nums, 0, pivot-1, target)
        else:
            return self.bin_search(nums, pivot, len(nums)-1, target)

    def bin_search(self, nums, l, r, target):
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1 

    def find_pivot(self, nums):
        l, r = 0, len(nums)-1
        pivot = 0
        while l <= r:
            if r - l < 2:
                if nums[r] < nums[l]:
                    return r
                return l
            pivot = (l+r)//2
            if nums[pivot-1] > nums[pivot] and nums[pivot+1] > nums[pivot]:
                return pivot
            if nums[l] <= nums[r]:
                return l
            elif nums[pivot] > nums[l] and nums[pivot] > nums[r]:
                l = pivot + 1
            else:
                r = pivot - 1
        return pivot