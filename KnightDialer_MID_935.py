"""
A chess knight can move as indicated in the chess diagram below:

 .



This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.



Example 1:

Input: 1
Output: 10
Example 2:

Input: 2
Output: 20
Example 3:

Input: 3
Output: 46


Note:

1 <= N <= 5000
"""


class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        552 ms
        """
        if N == 1:
            return 10
        temp = 10 ** 9 + 7
        dp = [[0] * 10 for _ in range(N)]
        for i in range(10):
            dp[0][i] = 1
        for i in range(1, N):
            dp[i][0] = (dp[i - 1][4] + dp[i - 1][6]) % temp
            dp[i][1] = (dp[i - 1][6] + dp[i - 1][8]) % temp
            dp[i][2] = (dp[i - 1][7] + dp[i - 1][9]) % temp
            dp[i][3] = (dp[i - 1][4] + dp[i - 1][8]) % temp
            dp[i][4] = (dp[i - 1][3] + dp[i - 1][9] + dp[i - 1][0]) % temp
            dp[i][6] = (dp[i - 1][1] + dp[i - 1][7] + dp[i - 1][0]) % temp
            dp[i][7] = (dp[i - 1][2] + dp[i - 1][6]) % temp
            dp[i][8] = (dp[i - 1][1] + dp[i - 1][3]) % temp
            dp[i][9] = (dp[i - 1][2] + dp[i - 1][4]) % temp

        s = 0
        for i in dp[-1]:
            s += i
            s %= temp
        return s

    def knightDialer_1(self, N):
        """
        :type N: int
        :rtype: int
        80ms  矩阵乘法，斐波那契数列的方法！！！！
        """
        import numpy as np
        mod = 10 ** 9 + 7
        if N == 1: return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]])
        res, N = 1, N - 1
        while N:
            if N % 2: res = res * M % mod
            M = M * M % mod
            N /= 2
        return int(np.sum(res)) % mod

print(Solution().knightDialer(1))
print(Solution().knightDialer(2))
print(Solution().knightDialer(3))
print(Solution().knightDialer(161))