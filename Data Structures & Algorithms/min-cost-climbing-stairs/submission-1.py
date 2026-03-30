class Solution:
    def __init__(self):
        self.memo = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        def min_cost_to_reach_index(i: int):
            if i < 2:
                return 0
            elif i in self.memo:
                return self.memo[i]
            else:
                prev_prev = min_cost_to_reach_index(i-2) + self.cost[i-2]
                prev = min_cost_to_reach_index(i-1) + self.cost[i-1]
                cost = min(prev_prev, prev)
                self.memo[i] = cost
                return cost
        return min(min_cost_to_reach_index(len(cost)-2)+cost[-2], min_cost_to_reach_index(len(cost)-1)+cost[-1])