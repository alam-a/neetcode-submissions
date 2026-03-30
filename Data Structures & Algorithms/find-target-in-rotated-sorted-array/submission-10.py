class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min_index(nums):
            l, r = 0, len(nums) - 1
            res = 0
            while l <= r:
                if nums[l] < nums[r]:
                    if nums[l] < nums[res]:
                        res = l
                    break
                mid = (l+r) // 2
                if nums[mid] < nums[res]:
                    res = mid
                if nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return res
        def binary_search(nums, l, r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        min_index = find_min_index(nums)
        left_check = binary_search(nums, 0, min_index - 1)
        if left_check == -1:
            return binary_search(nums, min_index, len(nums)-1)
        return left_check