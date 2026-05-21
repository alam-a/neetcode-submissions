class Solution:
    def __init__(self):
        self.memo = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        def cost_at_i(i: int):
            if i < 2:
                return 0
            elif i in self.memo:
                return self.memo[i]
            else:
                cost = min(cost_at_i(i-2), cost_at_i(i-1))+self.cost[i]
                self.memo[i] = cost
                return cost
        return min(cost_at_i(len(cost)-2)+cost[-2], cost_at_i(len(cost)-1)+cost[-1])