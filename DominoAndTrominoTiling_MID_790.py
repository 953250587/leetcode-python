"""
We have two types of tiles: a 2x1 domino shape, and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X

Given N, how many ways are there to tile a 2 x N board? Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input: 3
Output: 5
Explanation:
The five different ways are listed below, different letters indicates different tiles:
XYZ XXZ XYY XXY XYY
XYZ YYZ XZZ XYY XXY

Note:

    N  will be in range [1, 1000].

"""


class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        35MS
        """
        if N == 1:
            return 1
        if N == 2:
            return 2
        dp = [1 for _ in range(N + 1)]
        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % int(1e9 + 7)
        return dp[-1]

    def numTilings_1(self, N):
        """
        :type N: int
        :rtype: int
        95MS
        """
        import numpy as np
        if N == 1:
            return 1
        if N == 2:
            return 2
        if N % 2 == 1:
            k = (N - 2) // 2
            # a1,b1,c1
            start = np.array([1, 1, 2], dtype=np.int64)
        else:
            k = (N - 4) // 2
            # a2,b2,c2
            start = np.array([2, 3, 4], dtype=np.int64)
        A = np.array([[2, 3, 4], [1, 1, 2], [1, 1, 1]], dtype=np.int64)
        while k > 0:
            # 相当于转化为2进制
            if k % 2 == 1:
                start = np.dot(start, A) % 1000000007
            k //= 2
            A = A.dot(A) % 1000000007

        return int(np.dot(start, np.array([[2],[1],[1]], dtype=np.int64)) % 1000000007)



print(Solution().numTilings(10))
print(Solution().numTilings_1(10))