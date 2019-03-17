"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:

Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:

Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.
"""


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        199ms
        """
        l = int((N * 2) ** 0.5)
        ans = 1
        for i in range(2, l + 1):
            # print(2 * N - (i - 1) * i, i)
            if (2 * N - (i - 1) * i) % (2 * i) == 0:
                ans += 1
        return ans

    def consecutiveNumbersSum_1(self, N):
        """
        43ms
        :param N:
        :return:
        """
        res = 1
        i = 3
        while N % 2 == 0:
            N /= 2
        while i * i <= N:
            count = 0
            while N % i == 0:
                N /= i
                count += 1
            res *= count + 1
            i += 2
        return res if N == 1 else res * 2
print(Solution().consecutiveNumbersSum(5))
print(Solution().consecutiveNumbersSum(9))
print(Solution().consecutiveNumbersSum(15))

