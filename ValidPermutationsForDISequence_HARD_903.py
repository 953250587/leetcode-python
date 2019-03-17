"""
We are given S, a length n string of characters from the set {'D', 'I'}. (These letters stand for "decreasing" and "increasing".)

A valid permutation is a permutation P[0], P[1], ..., P[n] of integers {0, 1, ..., n}, such that for all i:

If S[i] == 'D', then P[i] > P[i+1], and;
If S[i] == 'I', then P[i] < P[i+1].
How many valid permutations are there?  Since the answer may be large, return your answer modulo 10^9 + 7.



Example 1:

Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)


Note:

1 <= S.length <= 200
S consists only of characters from the set {'D', 'I'}.
"""
class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
         784 ms n**3
         dp[i][j] 第i个位置的元素是剩下元素的第j+1位
        """
        n = len(S) + 1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(n - i):
                if S[i - 1] == 'D':
                    for k in range(j + 1, n - i + 1):
                        dp[i][j] += dp[i - 1][k]
                else:
                    for k in range(j + 1):
                        dp[i][j] += dp[i - 1][k]
                dp[i][j] %= 10**9 + 7
        # import numpy as np
        # print(np.array(dp))
        return dp[-1][0]

    def numPermsDISequence_1(self, S):
        """
        :type S: str
        :rtype: int
        52 ms n**2
        """
        n = len(S) + 1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, n):
            if S[i - 1] == 'D':
                dp[i][0] = sum([dp[i - 1][k] for k in range(1, n - i + 1)]) % (10**9 + 7)
                mark = -1
            else:
                dp[i][0] = dp[i - 1][0]
                mark = 1
            for j in range(1, n - i):
                dp[i][j] += mark * dp[i - 1][j] + dp[i][j - 1]
                dp[i][j] %= 10**9 + 7
        # import numpy as np
        # print(np.array(dp))
        return dp[-1][0]

print(Solution().numPermsDISequence_1("DID")) # 5
print(Solution().numPermsDISequence_1("IDDDIIDIIIIIIIIDIDID")) # 853197538
print(Solution().numPermsDISequence("DDIIDDIIIIIIIDIDIIII")) # 120119665
print(Solution().numPermsDISequence_1("DDIIDDIIIIIIIDIDIIII")) # 120119665
