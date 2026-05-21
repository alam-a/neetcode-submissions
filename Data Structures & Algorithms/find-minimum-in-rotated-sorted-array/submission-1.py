class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = float("inf")
        c = 0
        while l <= r:
            if c>50:
                break
            c+=1
            mid = l+(r-1)//2
            ln, mn, rn = nums[l], nums[mid], nums[r]
            print(ln, mn, rn)
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
