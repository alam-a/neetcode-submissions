class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0
        while l < r:
            res = max(res, (r-l) * min(heights[l], heights[r]))
            if heights[l+1] > heights[r-1]:
                l += 1
            elif heights[l+1] < heights[r-1]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res