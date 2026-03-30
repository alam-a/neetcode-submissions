class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        
        l, r = 1, max(piles)
        res = float("inf")
        while l <= r:
            mid = (l + r) // 2
            time = sum(map(lambda pile: math.ceil(pile/mid), piles))
            print(mid, time)
            if time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res