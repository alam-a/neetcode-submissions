class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = float("inf")
        while l <= r:
            mid = (l+r)//2
            ln, mn, rn = nums[l], nums[mid], nums[r]
            print(l, mid, r, ln, mn, rn)
            m = min(m, mn)
            if mn <= ln and mn <= rn:
                if ln > rn:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if ln < rn:
                    r = mid-1
                else:
                    l = mid+1
        return m