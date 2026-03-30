class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for num in nums:
            if num not in exists:
                exists.add(num)
            else:
                return True
        return False