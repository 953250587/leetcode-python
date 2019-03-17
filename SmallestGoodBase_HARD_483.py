"""
For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

Example 1:

Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.

Example 2:

Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.

Example 3:

Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.

Note:

    The range of n is [3, 10^18].
    The string representing n is always valid and will not have leading zeros.

"""


class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        446ms
        """
        num = int(n)
        max_l = len(bin(num)) - 2
        print(num, max_l)
        for i in range(max_l, 0, -1):
            high = num
            low = 2
            while low <= high:
                mid = (low + high) // 2
                val = mid ** i - num * mid
                if val > 1 - num:
                    high = mid - 1
                elif val < 1 - num:
                    low = mid + 1
                else:
                    return str(mid)
        # print(max_l)
        # print(int(n) + 1)

    def smallestGoodBase_1(self, n):
        """
        :type n: str
        :rtype: str
        47ms
        """
        import math
        n = int(n)
        m = int(math.log(n, 2))
        for k in range(m, 1, -1):
            base = int(n ** (1. / k)) # 找到最接近的整数值
            if (base ** (k + 1) - 1) // (base - 1) == n:
                return str(base)
        return str(n - 1)
print(Solution().smallestGoodBase('100000000000000000'))
print(Solution().smallestGoodBase('13'))
print(Solution().smallestGoodBase("4681"))
