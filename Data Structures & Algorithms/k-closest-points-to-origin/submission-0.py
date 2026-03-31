class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush_max, heappop_max
        heap = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heappush_max(heap, (distance, point))
            if len(heap) > k:
                heappop_max(heap)
        
        return [pi[1] for pi in heap]