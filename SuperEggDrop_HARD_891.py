"""
You are given K eggs, and you have access to a building with N floors from 1 to N.

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N).

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?



Example 1:

Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.
Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4


Note:

1 <= K <= 100
1 <= N <= 10000

"""


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        memo = {}
        def dfs(k, n):
            if (k, n) in memo:
                return memo[(k, n)]
            if k == 1:
                memo[(k, n)] = n
                return n
            if n <= 1:
                memo[(k, n)] = n
                return n
            # next_n = (n - 1) // 2
            memo[(k, n)] = float('inf')
            for i in range(1, n):
                a = dfs(k - 1, i) + 1
                b = dfs(k, n - 1 - i) + 1
                c = max(a, b)
                memo[(k, n)] = min(memo[(k, n)], c)
            return memo[(k, n)]

        ans = dfs(K, N)
        # print(memo)
        return ans


    def superEggDrop_1(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        for i in range(1, N + 1):
            dp[1][i] = i
        for j in range(1, K + 1):
            dp[j][1] = 1
        for i in range(2, K + 1):
            for j in range(2 , N + 1):
                dp[i][j] = float('inf')
                # 这边用线性查找就是kn**2的复杂度
                # for x in range(1, j + 1):
                #     c = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                #     dp[i][j] = min(dp[i][j], c)
                # 考虑到固定i，dp[i][j]随着j增大而增大，所以考虑2分查找
                # 复杂度knlogn,依旧超时= =
                lo, hi = 0, j
                result = float('inf')
                while lo < hi:
                    mid = (lo + hi) // 2
                    left, right = dp[i][mid - 1], dp[i - 1][j - mid]
                    result =min(result, 1 + max(dp[i][mid - 1], dp[i - 1][j - mid]))
                    if left < right:
                        lo = mid + 1
                    else:
                        hi = mid
                dp[i][j] = result
        return dp[-1][-1]

    def superEggDrop_2(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
         836 ms
        """
        # dp[M][K]means that, given K eggs and M moves,
        # what is the maximum number of floor that we can check.
        dp = [[0] * (K + 1) for i in range(N + 1)]
        for m in range(1, N + 1):
            for k in range(1, K + 1):
                # 如果在这层碎了，则我们可以检查这层以下的dp[m - 1][k - 1]层
                # 否则我们检查这层以上的dp[m - 1][k]
                # 再加上自己本身一层
                dp[m][k] = dp[m - 1][k - 1] + dp[m - 1][k] + 1
        for i in range(1, N + 1):
            if max(dp[i]) >= N:
                return i

    def superEggDrop_3(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        1180ms 不科学，有问题！！！
        """
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        for i in range(1, N + 1):
            dp[1][i] = i
            dp[0][i] = 0
        for j in range(1, K + 1):
            dp[j][1] = 1

        for i in range(2, K + 1):
            x = 1
            for j in range(2, N + 1):
                while x < j + 1:
                    if dp[i][x - 1] >= dp[i - 1][j - x]:
                        dp[i][j] = 1 + max(dp[i - 1][j - x], dp[i][x - 1])
                        break
                    x += 1
        return dp[-1][-1]


print(Solution().superEggDrop_1(K = 1, N = 2))
print(Solution().superEggDrop_1(K = 2, N = 3))
print(Solution().superEggDrop_1(K = 2, N = 6))
print(Solution().superEggDrop_1(K = 3, N = 14))
print(Solution().superEggDrop_1(2, 2))
print(Solution().superEggDrop_1(2, 9))
print(Solution().superEggDrop_1(100, 8191))