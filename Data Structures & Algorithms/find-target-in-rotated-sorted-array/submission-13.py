class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min() -> int:
            l, r = 0, len(nums) - 1
            res = 0
            while l <= r:
                if nums[l] <= nums[r]:
                    if nums[l] < nums[res]:
                        return l
                    return res
                mid = (l + r) // 2
                if nums[mid] < nums[res]:
                    res = mid 
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        pivot =  find_min()
        def bin_search(beg, end):
            while beg <= end:
                mid = (beg + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    beg = mid + 1
                else:
                    end = mid - 1
            return -1
        res = bin_search(0, pivot-1)
        if res == -1:
            res = bin_search(pivot, len(nums)-1)
        return res

