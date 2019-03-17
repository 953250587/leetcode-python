"""
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Note: You can assume that

0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1


Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.


Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if coins == []:
            return 1 if amount == 0 else 0
        memory = {}
        def dfs(cur_amount, i):
            if (cur_amount, i) in memory:
                return memory[(cur_amount, i)]
            if cur_amount == amount:
                return 1
            if i == len(coins) - 1:
                if (amount - cur_amount) % coins[i] == 0:
                    return 1
                else:
                    return 0
            k = 0
            ans = 0
            while cur_amount + k * coins[i] <= amount:
                ans += dfs(cur_amount + k * coins[i], i + 1)
                k += 1
            memory[(cur_amount, i)] = ans
            return ans
        return dfs(0, 0)

    def change_1(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        280 ms
        """
        if coins == []:
            return 1 if amount == 0 else 0
        coins.sort()
        ways = [0] * (amount + coins[-1] + 1)  # usually coins[-1] small vs amount, saves if statement
        ways[0] = 1
        for c in coins:  # forces order by coin count.
            for i in range(amount + 1):
                ways[i + c] += ways[i]
        return ways[amount]

    def change_2(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        64ms
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for value in range(coin, amount + 1):
                v = dp[value - coin]
                if v:
                    dp[value] += v
        return dp[amount]
print(Solution().change(amount = 5, coins = [1, 2, 5]))
print(Solution().change(amount = 3, coins = [2]))
print(Solution().change(amount = 10, coins = [10]))
print(Solution().change(5000, [1,2]))