class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)

        def time_taken(speed):
            return sum(map(lambda pile: math.ceil(pile / speed), piles))
        
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            if time_taken(mid) <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res

