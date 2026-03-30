class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, float("inf")
        while l <= r:
            mid = (l+r)//2
            print(l, r, mid, nums[mid])
            res = min(res, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return res