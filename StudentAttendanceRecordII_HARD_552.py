"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

    'A' : Absent.
    'L' : Late.
    'P' : Present.

A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:

Input: n = 2
Output: 8
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.

Note: The value of n won't exceed 100,000.

"""
class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        1276 ms
        """
        if n == 0:
            return 0
        if n == 1:
            return 3
        # dp = [2, 1, 1, 3, 1, 0]
        # for i in range(3, n + 1):
        #     # cur_dp = [0, 0, 0, 0, 0, 0]
        #     s_1, s_2 = 0, 0
        #     for i in range(3):
        #         s_1 += dp[i] % (1e9 + 7)
        #         s_2 += dp[i + 3] % (1e9 + 7)
        #     dp[2] = dp[1]
        #     dp[1] = dp[0]
        #     dp[0] = s_1
        #
        #     dp[5] = dp[4]
        #     dp[4] = dp[3]
        #     dp[3] = (s_1 % (1e9 + 7) + s_2 % (1e9 + 7)) % (1e9 + 7)
        #
        #     # dp = cur_dp
        # return int(sum(dp) % (1e9 + 7))
        dp = [1, 1, 2]
        ans = 0
        for i in range(2, n):
            dp.append(sum(dp[i - 2:]) % (1000000007))
        # 记以P为结尾的状态为1， 记以L为结尾的状态为2，记以LL为结尾的状态为3，
        #  下一次P为结尾 为之前状态之和， 以L为结尾的状态为P为结尾的状态的个数， 以Ll为结尾的状态为l为结尾的状态的个数
        # 所以可以用dp为每个n的总和（从dp[1]开始记录，dp【i】表示第i-1时候的总个数）
        ans += sum(dp[-3:]) % (1000000007)
        for i in range(n):
            ans += dp[i + 1] * dp[n - i] % (1000000007)
            ans %= (1000000007)
        return ans

    def checkRecord_1(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i - 1] + nums[i - 2]) % 1000000007)
            i += 1
        result = (nums[n] + nums[n - 1] + nums[n - 2]) % 1000000007
        for i in range(n):
            result += nums[i + 1] * nums[n - i] % 1000000007
            result %= 1000000007
        return result


print(Solution().checkRecord(100))
print(Solution().checkRecord_1(100))
print(Solution().checkRecord(88900))

import numpy as np


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        89ms
        """
        modVal = 1000000007

        #         f = (
        #             (1, 0),
        #             (0, 0),
        #             (0, 0)
        #         )
        #         for i in range(n):
        #             f = (
        #                  ((f[0][0] + f[1][0] + f[2][0]) % modVal, (f[0][0] + f[0][1] + f[1][0] + f[1][1] + f[2][0] + f[2][1]) % modVal),
        #                 f[0],
        #                 f[1]
        #              )

        #         ans =  (f[0][0] + f[0][1] + f[1][0] + f[1][1] + f[2][0] + f[2][1]) % modVal
        #         return ans
        A = np.array(
            [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0]], dtype=np.int64)
        x = np.array([1, 0, 0, 0, 0, 0], dtype=np.int64)
        res = np.eye(6, dtype=np.int64)
        while n:
            if n & 1 == 1:
                # res = (res+A.dot(x))%modVal
                res = res.dot(A) % modVal
            A = A.dot(A) % modVal
            n >>= 1
        return int(np.sum(res.dot(x)) % modVal)