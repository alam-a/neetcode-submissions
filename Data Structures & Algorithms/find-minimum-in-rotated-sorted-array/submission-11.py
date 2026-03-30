class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")
        count = 0
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r) // 2
            print(l, r, mid, nums[l], nums[r], nums[mid])
            res = min(res, nums[mid])
            if nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return res