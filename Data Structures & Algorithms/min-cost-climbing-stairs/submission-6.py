class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        L = len(cost)
        prev, prev_prev = 0, 0
        for i in range(2, L):
            prev, prev_prev = min(prev + cost[i-1], prev_prev + cost[i-2]), prev
        
        return min(prev + cost[L-1], prev_prev + cost[L-2])