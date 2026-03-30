import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        last = None
        for _ in range(k):
            last = heapq.heappop_max(nums)
        return last