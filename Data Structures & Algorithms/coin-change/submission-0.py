class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        def dfs(index, value, noc):
            if value == amount:
                return noc
            if value > amount:
                return -1
            for i in range(index, len(coins)):
                temp = dfs(i, value + coins[i], noc + 1)
                if temp != -1:
                    return temp
            return -1
        return dfs(0, 0, 0)