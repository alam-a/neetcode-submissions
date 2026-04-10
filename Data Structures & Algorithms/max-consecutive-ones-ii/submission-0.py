class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L, l, r = len(nums), 0, 0
        res = 0
        zc = 0 # zero count
        while r < L:
            if nums[r] == 0:
                zc += 1
            while zc > 1:
                if nums[l] == 0: # till number of 1 becomes less than 2, slide l
                    zc -= 1
                    l += 1
                    break
                l += 1
            res = max(res, r - l + 1)
            r += 1 # slides right
        return res