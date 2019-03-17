"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        37ms
        """
        if n == 0:
            return 0
        import math
        k = int(math.log(n, 5))
        # print(k)
        # ans = n // 5 * ((1 - 0.2 ** k) / 0.8)
        # return int(ans)
        ans = 0
        for i in range(1, k + 1):
            ans += n // 5 ** i
        return ans

# print(Solution().trailingZeroes(624))
# for i in range(1, 20):
#     print(i, Solution().trailingZeroes(i))
# print(Solution().trailingZeroes(50))
print(Solution().trailingZeroes(1000000000))