"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation:
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.



Note:

    1 <= A.length <= 100.
    1 <= A[i] <= 10000.
    1 <= K <= A.length.
    Answers within 10^-6 of the correct answer will be accepted as correct.


"""


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        944ms
        """
        M = len(A)
        # dp记录分成K份，最后一份为m个元素的前面K-1的最大平均数之和与最后一份的平均数
        dp = [[(0, 0) for _ in range(M + 1)] for _ in range(K + 1)]
        dp[1][1] = (0, A[0])
        # 从第二个数开始
        for i in range(2, M + 1):
            # 新建一个dp数组
            dp2 = [[(0, 0) for _ in range(M + 1)] for _ in range(K + 1)]
            # 计算K=1的情况
            avg = (dp[1][i - 1][1] * (i - 1) + A[i - 1]) / i
            dp2[1][i] = (0, avg)
            max_1 = 0
            # 考虑K>=2的情况
            for k in range(2, min(K + 1, i + 1)):
                # 最后一组元素的个数，最大不会超过编号i
                for m in range(1, i):
                    # 如果k没有超过最大分组数，则还可以新建分组。考虑所有情况分组的最大平均值
                    max_1 = max(dp[k - 1][m][0] + dp[k - 1][m][1], max_1)
                    # 计算保证K分组的情况，最后一个分组加上新元素
                    if m > 1:
                        dp2[k][m] = (dp[k][m - 1][0], (dp[k][m - 1][1] * (m - 1) + A[i - 1]) / m)
                dp2[k][1] = (max_1, A[i - 1])
            dp = dp2
        ans = 0
        # 所有K分组中最大平均数之和
        for i in dp[K]:
            ans = max(i[0] + i[1], ans)
        return ans

    def largestSumOfAverages_1(self, A, K):
        """
        963ms
        :param A:
        :param K:
        :return:
        """
        memo = {}

        def search(n, k):
            if (n, k) in memo: return memo[n, k]
            if k == 1:
                memo[n, k] = sum(A[:n]) / float(n)
                return memo[n, k]
            cur, memo[n, k] = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]

        return search(len(A), K)
print(Solution().largestSumOfAverages(A = [9,1,2,3,9], K = 3))
print(Solution().largestSumOfAverages([9], 1))

