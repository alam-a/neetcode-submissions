class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, total = 0, 0, 0
        res = 0
        while r < len(nums):
            total += nums[r]
            print(l, r, total)
            if total >= target:
                if res == 0:
                    res = r - l + 1
                else:
                    res = min(res, r - l + 1)
            while total - nums[l] >= target:
                total -= nums[l]
                l += 1
                res = min(res, r - l + 1)
            r += 1
        return res
            