"""
 You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if coins == [] or amount == 0:
            return 0
        coins=sorted(coins)
        dp=[-1 for i in range(amount+1)]
        for i in range(coins[0],amount+1):
            if i in coins:
                dp[i]=1
            else:
                for k in range(1,i//2+1):
                    print(k,i)
                    if dp[i-k]!=-1 and dp[k]!=-1:
                        if dp[i]==-1:
                            dp[i]=dp[i-k]+dp[k]
                        else:
                            dp[i]=min(dp[i-k]+dp[k],dp[i])
        print(dp)
        return dp[amount]

    def coinChange_1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        572ms
        bfs
        """
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1

    def coinChange_2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        269ms
        dfs
        """
        coins.sort(reverse=True)
        n, self.res = len(coins), 2 ** 31 - 1

        def dfs(idx, rem, count):
            if rem == 0:
                self.res = min(self.res, count)
                return
            for i in range(idx, n):
                if coins[i] <= rem < coins[i] * (self.res - count):  # if hope still exists
                    dfs(i, rem - coins[i], count + 1)

        for idx in range(n):
            dfs(idx, amount, 0)
        return self.res if self.res < 2 ** 31 - 1 else -1

    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        1499 ms
        dp
        """
        coins.sort()

        INF = 0x7fffffff  # Using float("inf") would be slower.
        amounts = [INF] * (amount + 1)
        amounts[0] = 0
        for i in range(amount + 1):
            if amounts[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        amounts[i + coin] = min(amounts[i + coin], amounts[i] + 1)
                    else:
                        break
        return amounts[amount] if amounts[amount] != INF else -1
coins = [1]
amount = 2
print(Solution().coinChange(coins,amount))