class Solution:
    def maxArea(self, heights: List[int]) -> int:
        print(heights)
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            print(l, r, heights[l], heights[r])
            res = max(res, (r - l) * min(heights[l], heights[r]))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1 
                r -= 1
        return res