class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = self.find_min_index(nums)
        print(min_index, nums[min_index])
        if nums[min_index] <= target <= nums[-1]:
            return self.binary_search(nums, min_index, len(nums)-1, target)
        else:
            return self.binary_search(nums, 0, min_index-1, target)

    def binary_search(self, nums, l, r, target):
        print("binary search starts")
        while l <= r:
            mid = (l+r)//2
            print(l, r, mid, nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return -1

    def find_min_index(self, nums):
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            print(l, r, nums[mid], nums[r])
            if nums[mid] > nums[r]:
                l = mid+1
                print(f"l={l}")
            else:
                r = mid
        return l