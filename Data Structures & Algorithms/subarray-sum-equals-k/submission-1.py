class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = defaultdict(int)
        total = 0
        count = 0
        res[0] = 1
        for num in nums:
            total += num
            count += res[total - k]
            res[total] += 1
        return count