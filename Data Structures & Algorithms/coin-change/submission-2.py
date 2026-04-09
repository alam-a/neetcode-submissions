class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = [float('inf')] * (amount+1)
        res[0] = 0
        for am in range(1, amount+1):
            for coin in coins:
                if am - coin >= 0:
                    res[am] = min(res[am], res[am - coin] + 1)
        if res[amount] == float('inf'):
            return -1
        return res[amount]