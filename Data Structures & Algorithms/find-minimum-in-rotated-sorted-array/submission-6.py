class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        m = float("inf")
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                m = min(m, nums[l])
                break
            mid = (l+r)//2
            m = min(m, nums[mid])
            print(nums[l], nums[mid], nums[r])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return m