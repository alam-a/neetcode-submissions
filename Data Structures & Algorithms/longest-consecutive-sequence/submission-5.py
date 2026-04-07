class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in num_set:
                count = 0
                temp = num
                while temp in num_set:
                    num_set.remove(temp)
                    temp += 1
                    count += 1
                res = max(res, count)
        return res