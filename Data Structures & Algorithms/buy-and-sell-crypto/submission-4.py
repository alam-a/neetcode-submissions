class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0
        for curr_price in prices[1:]:
            if buy_price > curr_price:
                buy_price = curr_price
            elif buy_price < curr_price:
                profit = max(curr_price - buy_price, profit)
        return profit