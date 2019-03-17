"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""
import math
class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        896ms
        """
        self.min=n

        def find_min(n,min_sum):
            if min_sum>=self.min:
                return
            r = math.sqrt(n) // 1
            if r ** 2 == n:
                self.min=min_sum
                return
            for i in range(1, int(r) + 1)[::-1]:
                find_min(n - i ** 2, min_sum + 1)

                # print(min_sum,n - i ** 2)

        find_min(n,1)
        return self.min

    def numSquares_1(self, n):
        """
        :type n: int
        :rtype: int
        228ms
        """
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp
        return cnt

    _dp = [0]

    def numSquares_3(self, n):
        # 152ms
        #dp[i]表示第i个数字的最小prefect square数
        dp = self._dp
        while len(dp) <= n:
            # 对每个位置，记录下这个位置与每个i的-i * i之差对应位置中的最小数，然后+1
            dp += min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,
        return dp[n]


print(Solution().numSquares_3(61))