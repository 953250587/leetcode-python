"""
Your music player contains N different songs and she wants to listen to L (not necessarily different) songs during your trip.  You create a playlist so that:

Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
Example 2:

Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
Example 3:

Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]


Note:

0 <= K < N <= L <= 100
"""


class Solution(object):
    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        120 ms
        """
        dp = [[0 for _ in range(L + 1)] for _ in range(N + 1)]
        dp[1][1] = 1
        # N和L相等情况就是一个阶乘形式
        for i in range(2, N + 1):
            dp[i][i] = dp[i - 1][i - 1] * i % (10 ** 9 + 7)
        for i in range(2, L + 1):
            # N不大于L
            for j in range(1, min(i, N + 1)):
                # 前段表示这首歌是第一次出现，后半段表示这首歌已经在之前使用过
                dp[j][i] = (dp[j - 1][i - 1] * j + dp[j][i - 1] * max(j - K, 0)) % (10 ** 9 + 7)
        print(dp)
        return dp[-1][-1]

    def numMusicPlaylists_1(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        36ms
        """
        factorial = [1]
        for i in range(N):
            factorial.append(len(factorial) * factorial[-1])
        p = 1
        res = 0
        for i in range(N, K, -1):
            res += factorial[-1] * (i - K) ** (L - K) * p // factorial[-1 - i] // factorial[i - K]
            p = -p
        return res % (10 ** 9 + 7)



print(Solution().numMusicPlaylists(N = 3, L = 3, K = 1))
print(Solution().numMusicPlaylists(N = 2, L = 3, K = 0))
print(Solution().numMusicPlaylists(N = 2, L = 3, K = 1))