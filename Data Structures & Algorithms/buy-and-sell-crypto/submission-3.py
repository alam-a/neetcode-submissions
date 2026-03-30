class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp, profit = prices[0], 0
        for price in prices[1:]:
            if bp > price:
                bp = price
            else:
                profit = max(profit, price-bp)
        return profit