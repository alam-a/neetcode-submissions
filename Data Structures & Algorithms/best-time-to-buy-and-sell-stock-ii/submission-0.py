class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bp, sp, tp = prices[0], prices[0], 0
        for price in prices:
            if price < sp:
                tp += (sp - bp)
                bp = price
            sp = price
        return tp + (sp - bp)