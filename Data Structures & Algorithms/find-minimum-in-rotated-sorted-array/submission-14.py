class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = 10000
        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return res