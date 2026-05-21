class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        res_len = (len(nums) - k + 1)
        res = [0] * res_len
        for i in range(res_len):
            heap = nums[i:i+k]
            heapq.heapify_max(heap)
            res[i] = heap[0]
        return res