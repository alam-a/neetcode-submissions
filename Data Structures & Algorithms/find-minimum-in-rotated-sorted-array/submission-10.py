class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, res = 0, len(nums)-1, float("inf")
        while l <= r:
            if nums[l] < nums[r]:
                return min(nums[l], res)
            mid = (l+r)//2
            res = min(nums[mid], res)
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid-1
        return res