"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

    The given numbers of 0s and 1s will both not exceed 100
    The size of given string array won't exceed 600.

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

"""
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        4135ms
        """
        l=len(strs)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        # for i in strs:
        #     a=i.count('0')
        #     if a<=m and len(i)-a<=n:
        #         dp[a][len(i)-a]=1
        print(dp)
        for i in range(1, l + 1):
            a = strs[i - 1]
            b = a.count('0')
            l = len(a)
            for j in range(m, b-1, -1):
                for k in range(n,l-b-1,-1):
                    dp[j][k] = max(dp[j][k], dp[j - b][k - (l - b)] + 1)
            print(dp)
        return dp[-1][-1]

    def findMaxForm_1(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        552ms
        """
        strs = sorted(strs, key=lambda x: (-len(x), x))
        return self.dfs(strs, 0, m, n, {})

    def dfs(self, strs, index, m, n, cache):
        if index == len(strs) or (m == 0 and n == 0):
            return 0
        if (index, m, n) in cache:
            return cache[(index, m, n)]

        res = 0
        for i in range(index, len(strs)):
            if i > index and strs[i] == strs[i - 1]:
                continue
            zero, one = strs[i].count('0'), strs[i].count('1')
            if m >= zero and n >= one:
                res = max(res, self.dfs(strs, i + 1, m - zero, n - one, cache) + 1)
        cache[(index, m, n)] = res
        return res

    def findMaxForm_2(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        3312ms
        """
        dp = [[0] * (n + 1) for x in range(m + 1)]
        for s in strs:
            zero, one = s.count('0'), s.count('1')
            for x in range(m, zero - 1, -1):
                for y in range(n, one - 1, -1):
                    dp[x][y] = max(dp[x - zero][y - one] + 1, dp[x][y])
        return dp[m][n]

print(Solution().findMaxForm(["10", "0001", "111001", "1", "0"],5,3))
print(Solution().findMaxForm(["10", "0", "1"],1,1))
print(Solution().findMaxForm([],1,1))
