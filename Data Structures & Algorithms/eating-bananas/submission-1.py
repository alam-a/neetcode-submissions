class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        def time_to_finish_pile(h: int):
            return sum(map(lambda n: math.ceil(n/h), piles))
        
        l, r = 1, h
        res = float("inf")
        while l < r:
            mid = (l + r) // 2
            time = time_to_finish_pile(h)
            if time < h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res