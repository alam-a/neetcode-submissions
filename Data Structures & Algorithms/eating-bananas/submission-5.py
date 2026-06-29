class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        def hours_to_eat(speed: int) -> int:
            return sum(map(lambda pile: math.ceil(pile/speed), piles))
        
        res = max(piles)
        l, r = 1, res
        while l <= r:
            mid = (l + r) // 2
            hours_at_pace = hours_to_eat(mid)
            # print(l, r, mid, hours_at_pace)
            if hours_at_pace <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res