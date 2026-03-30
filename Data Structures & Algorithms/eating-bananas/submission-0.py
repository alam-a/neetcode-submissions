class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        from functools import reduce
        def total_time_per_eating_speed(es: int) -> int:
            return reduce(lambda x, y: x+y, map(lambda pile: math.ceil(pile/es), piles))
        
        if len(piles) == h:
            return max(piles)
        
        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            mid = (l+r)//2
            time = total_time_per_eating_speed(mid)
            if time <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return int(res)