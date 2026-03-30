class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.res = {0: 0, 1: 0}
        def min_cost_at_index(i):
            if i < 0:
                return 0
            if i in self.res:
                return self.res[i]
            slast = min_cost_at_index(i-2)+cost[i-2]
            last  = min_cost_at_index(i-1)+cost[i-1]
            self.res[i] = min(last, slast)
            return self.res[i]
        return min_cost_at_index(len(cost))