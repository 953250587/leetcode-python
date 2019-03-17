"""
 Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        32ms
        """
        dp=[0 for i in range(n+1)]
        if n==2:
            return 1
        dp[1]=1
        dp[2]=1
        for i in range(3,n+1):
            for j in range(1,i//2+1):
                dp[i]=max(dp[i],max(dp[j],j)*max(dp[i-j],i-j))
        return dp[-1]

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        28ms
        """
        res = 0
        for i in range(2, n + 1):
            a1 = n // i
            if n % i == 0:
                res = max(res, a1 ** i)
            else:
                a2 = a1 + 1
                n2 = n % i
                n1 = i - n2
                res = max(res, (a1 ** n1) * (a2 ** n2))
        return res
print(Solution().integerBreak(10))