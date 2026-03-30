class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         largest = max(largest, min(heights[i], heights[j]) * (j - i))
        # return largest
        l, r = 0, len(heights)-1
        while l < r:
            largest = max(largest, min(heights[l], heights[r]) * (r - l))
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
        return largest