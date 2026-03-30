from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            l, sl = heappop_max(stones), heappop_max(stones)
            diff = abs(l - sl)
            if diff:
                heappush_max(stones, diff)
        return stones[0] if stones else 0