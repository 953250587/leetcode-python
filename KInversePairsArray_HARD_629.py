"""
 Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation:
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation:
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Note:

    The integer n is in the range [1, 1000] and k is in the range [0, 1000].

"""

import numpy as np
class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        784MS
        """
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][0] = 1
        for i in range(2, n + 1):
            a = 0
            for j in range(k + 1):
                a += dp[i - 1][j] % MOD
                a %= MOD
                if j - i >= 0:
                    a -= dp[i - 1][j - i] % MOD
                a %= MOD
                dp[i][j] = a
        # print(np.array(dp))
        return dp[n][k]

    def kInversePairs_1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        344MS
        """

        prev = [1] + [0] * k
        m = 10 ** 9 + 7
        for j in range(2, n + 1):

            new = [0] * (k + 1)
            s = 0
            for i in range(k + 1):
                s += prev[i]
                if i >= j:
                    s -= prev[i - j]
                if not s: # 早点跳出，比我优化了
                    break
                new[i] = s % m
            prev = new

        return prev[k]
# print(Solution().kInversePairs(5, 10))
# print(Solution().kInversePairs(3, 0))
# print(Solution().kInversePairs(3, 1))
print(Solution().kInversePairs(1000, 3))
