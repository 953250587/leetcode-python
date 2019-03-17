"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
Credits:
"""


class Solution(object):
    def maxProfit(self, numbers):
        """
        :type prices: List[int]
        :rtype: int
        42MS
        """
        if len(numbers) <= 0:
            return 0
        dp = [[0, 0, 0] for i in range(len(numbers))]
        res = 0
        dp[0][2] = -numbers[0]
        for i in range(1, len(numbers)):
            dp[i][0] = dp[i - 1][2] + numbers[i]
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] - numbers[i], dp[i - 1][2])
        # print(dp)
        return max(dp[-1][0], dp[-1][1], dp[-1][2])
