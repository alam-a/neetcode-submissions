class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush_max, heappop_max, heapify_max
        heapify_max(stones)
        while stones:
            if len(stones) > 1:
                largest = heappop_max(stones)
                next_largest = heappop_max(stones)
                if largest != next_largest:
                    heappush_max(stones, largest - next_largest)
            else:
                return stones[0]
        return 0