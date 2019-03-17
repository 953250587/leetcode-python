"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if  n==1:
            return 10
        sum_1=10
        val=9
        if n>9:
            n=9
        if n<=9:
            for i in range(1,n):
                val*=10-i
                sum_1+=val
        return sum_1

    def countNumbersWithUniqueDigits_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        ans = 10
        base = 9
        for i in range(2, min(n + 1, 11)):
            base *= 11 - i
            ans += base
        return ans
print(Solution().countNumbersWithUniqueDigits(3))

