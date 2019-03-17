"""
 Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:

Input:
S = 'bccb'
Output: 6
Explanation:
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:

Input:
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation:
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:
The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""


class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        1323MS
        """
        N = len(S)
        A = [ord(c) - ord('a') for c in S]
        prv = [None] * N
        nxt = [None] * N

        last = [None] * 4
        for i in range(N):
            last[A[i]] = i
            prv[i] = tuple(last)

        last = [None] * 4
        for i in range(N - 1, -1, -1):
            last[A[i]] = i
            nxt[i] = tuple(last)

        print(prv)
        print(nxt)
        MOD = 10 ** 9 + 7
        memo = [[None] * N for _ in range(N)]

        def dp(i, j):
            if memo[i][j] is not None:
                return memo[i][j]
            ans = 1  # The empty-string palindrome
            if i <= j:
                for x in range(4):  # For letter a, b, c, d ...
                    i0 = nxt[i][x]
                    j0 = prv[j][x]
                    if i <= i0 <= j:
                        ans += 1  # The letter x exists in [i, j]
                    if None < i0 < j0:
                        ans += dp(i0 + 1, j0 - 1)  # Counting palindromes "x_x"
            ans %= MOD
            memo[i][j] = ans
            return ans

        return dp(0, N - 1) - 1  # Subtract empty string

    def countPalindromicSubsequences_1(self, S):
        """
        :type S: str
        :rtype: int
        2571MS
        """
        l = len(S)
        dp = [[0] * l for _ in range(l)]  # 从i到j不重复的回文数

        for i in range(l):
            dp[i][i] = 1

        for distance in range(1, l):
            for i in range(l - distance):
                j = i + distance
                if S[i] == S[j]:
                    low = i + 1
                    high = j - 1
                    while low <= high and S[low] != S[j]:
                        low += 1
                    while low <= high and S[high] != S[j]:
                        high -= 1
                    if low > high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif low == high:
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[low + 1][high - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
            dp[i][j] = dp[i][j] + 1000000007 if dp[i][j] < 0 else dp[i][j] % 1000000007
        return dp[0][l - 1]
print(Solution().countPalindromicSubsequences_1('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'))
print(Solution().countPalindromicSubsequences_1('bccb'))