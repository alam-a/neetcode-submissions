class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        v = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in v:
                curr = 0
                curr_val = num 
                while curr_val in  v:
                    curr_val += 1
                    curr += 1
                res = max(res, curr)
        return res