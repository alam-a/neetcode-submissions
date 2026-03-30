class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unums, res = set(nums), 0
        for num in nums:
            if num - 1 not in unums:
                temp = num
                while temp in unums:
                    unums.remove(temp)
                    temp += 1
                res = max(res, temp - num)
        return res