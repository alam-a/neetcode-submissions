from functools import lru_cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1


        # # inefficient
        # @lru_cache
        # def min_coins(target):
        #     if target == 0:
        #         return 0
        #     if targecache, t < 0:
        #         return float("inf")
        #     res = float("inf")
        #     for coin in coins:
        #         res = min(res, 1 + min_coins(target - coin))
        #     return res
        # res = min_coins(amount)
        # return res if res != float("inf") else -1


            # if target in cache:
            #     return cache[target]
        #     res = -1
        #     for coin in coins:
        #         curr = target - coin
        #         print(curr, cache)
        #         if curr >= 0:
        #             if curr not in cache:
        #                 cache[curr] = min_coins(curr)
        #             if cache[curr] != -1:
        #                 if res == -1:
        #                     res = 1 + cache[curr]
        #                 else:
        #                     res = min(res, 1 + cache[curr])
        #     return res
        # cache[amount] = min_coins(amount)
        # return cache[amount]