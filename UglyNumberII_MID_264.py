"""

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        185ms
        """
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

    ugly = sorted(2 ** a * 3 ** b * 5 ** c
                  for a in range(32) for b in range(20) for c in range(14)) # 投机取巧

    def nthUglyNumber_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.ugly[n - 1]
