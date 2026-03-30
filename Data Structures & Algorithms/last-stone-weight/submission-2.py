class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        import heapq
        heapq.heapify(stones)

        while len(stones)>1:
            h = heapq.heappop(stones)
            sh = heapq.heappop(stones)
            if h != sh:
                heapq.heappush(stones, -abs(h-sh))
        return 0 if not stones else -stones[0]
            


