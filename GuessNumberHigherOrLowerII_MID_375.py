"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.
"""
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        1335
        """
        if n==1:
            return 0
        self.dp=[[float('inf') for i in range(n+1)] for j in range(n+1)]
        for i in range(1,n):
            self.dp[i][i] = 0
            self.dp[i][i-1]=0
            self.dp[i][i+1]=i
            if i<n-1:
               self.dp[i][i+2]=i+1
        for length in range(3,n):
            for i in range(1,n-length+1):
                for k in range(i,i+length+1):
                    if k-1<i:
                        a=0
                    else:
                        a=self.dp[i][k-1]
                    if k+1>i+length:
                        b=0
                    else:
                        b=self.dp[k+1][i+length]
                    self.dp[i][i+length]=min(k+max(a,b),self.dp[i][i+length])
        # print(self.dp)
        return self.dp[1][-1]

    def getMoneyAmount_1(self, n):
        """
        :type n: int
        :rtype: int
        235ms
        """
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        def dphelper(s, e):
            if s >= e:
                return 0
            if dp[s][e]:
                return dp[s][e]
            ret = float('inf')
            mid = (s + e) / 2
            for m in range(mid, e + 1):
                tmp = m + max(dphelper(s, m - 1), dphelper(m + 1, e))
                ret = min(ret, tmp)
            dp[s][e] = ret
            return ret

        return dphelper(1, n)
print(Solution().getMoneyAmount(5))