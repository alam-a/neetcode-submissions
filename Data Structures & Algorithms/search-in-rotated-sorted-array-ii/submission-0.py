class Solution:
    def search(self, nums: List[int], target: int) -> bool:
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

        def fin_min_index():
            l, r = 0, len(nums)-1
            res = 0
            while l <= r:
                if nums[l] <= nums[r]:
                    if nums[res] < nums[l]:
                        res = l
                    break
                mid = (l + r) // 2
                if nums[res] < nums[mid]:
                    res = mid
                if nums[l] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return res             
        pivot = fin_min_index()
        print(pivot, nums[pivot])
        if bin_search(0, pivot-1) == -1 and bin_search(pivot, len(nums)-1) == -1:
            return False
        return True
