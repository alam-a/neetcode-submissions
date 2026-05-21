class Solution:
    def findMin(self, nums: List[int]) -> int:
        m = float("inf")
        l, r = 0, len(nums)-1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l+r)//2
            m = min(m, nums[mid])
            if nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return m