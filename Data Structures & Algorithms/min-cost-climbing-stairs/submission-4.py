class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        slast, last = 0, 0
        for i in range(2, len(cost)):
            temp = last
            last = min(slast+cost[i-2], last+cost[i-1])
            slast = temp
        return min(slast+cost[-2], last+cost[-1])