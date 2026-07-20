class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        l, r = 0, 0
        while r < len(nums):
            if nums[r] in seen:
                return True
            seen.add(nums[r])
            if not len(seen) < k:
                seen.remove(nums[l])
                l += 1
            r += 1
        return False