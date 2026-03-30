class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_minimum_index():
            l, r = 0, len(nums)-1
            res = 0
            while l <= r:
                if nums[l] < nums[r]:
                    return l
                mid = (l + r) // 2
                if nums[mid] < nums[res]:
                    res = mid
                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return res
        def find(l: int, r: int) -> int:
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1
        min_index = find_minimum_index()
        print(min_index, nums[min_index])
        res = find(0, min_index-1)
        if res != -1:
            return res
        return find(min_index, len(nums)-1)