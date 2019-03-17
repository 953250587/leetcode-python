"""
 Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"

Output:

4

One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:

"cbbd"

Output:

2

One possible longest palindromic subsequence is "bb".
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dicts={}
        count=0
        for char in s:
            if char not in self.dicts.keys():
                self.dicts[char]=[count]
            else:
                self.dicts[char].append(count)
            count+=1
        l=len(s)
        self.max=1
        self.dp=[-1]*(l+1)
        self.dp_start = [-1] * (l + 1)
        self.dp[1]=self.dicts[s[0]][-1]
        self.dp_start[1]=self.dicts[s[0]][0]
        self.dp_num=1
        self.count=0
        for char in s[1:]:
            self.count+=1
            for i in range(2,self.dp_num+2)[::-1]:
                for k in self.dicts[char][::-1]:
                    if k<self.dp[i-1] and k>self.dp_start[i-1]:
                        if self.dp[i]<k:
                            self.dp[i]=k
                            self.dp_start[i]=self.count
                        self.dp_num=max(self.dp_num,i)
                        if self.dp[i] != -1 and self.dp_start[i] != self.dp[i]:
                            self.max = max(self.max, 2 * i)
                        elif self.dp[i] != -1 and self.dp_start[i] == self.dp[i]:
                            self.max = max(self.max, 2 * i - 1)
                        break
                    elif k<=self.dp_start[i-1]:
                        break
            if self.dp[1]<self.dicts[char][-1]:
                self.dp_start[1]=self.count
                self.dp[1]=self.dicts[char][-1]
            if self.dp_start[1] != self.dp[1]:
                self.max = max(self.max, 2)
            print(self.count, self.dp_start, self.max,self.dp_num)
            print(self.count,self.dp,self.max,self.dp_num)
        return self.max

    def longestPalindromeSubseq_1(self, s):
        """
        :type s: str
        :rtype: int
        1319ms
        """
        if s==s[::-1]:
            return len(s)
        l = len(s)
        self.dp=[[1 for i in range(l)] for i in range(l)]
        for length in range(1,l):
            for i in range(0,l-length):
                # print((i,i+length))
                if s[i]==s[i+length]:
                    if i+1<=i+length-1:
                        a=self.dp[i+1][i+length-1]
                    else:
                        a=0
                    self.dp[i][i+length]=a+2
                else:
                    a = self.dp[i + 1][i+length]
                    b = self.dp[i][i+length - 1]
                    self.dp[i][i+length] = max(self.dp[i][i+length], a, b)
                # print(self.dp)
        return self.dp[0][-1]

    def longestPalindromeSubseq_2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]:
            return len(s)
        n = len(s)
        dp = [0 for j in range(n)]
        dp[n - 1] = 1
        for i in range(n - 1, -1, -1):  # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j - 1]
                else:
                    newdp[j] = max(dp[j], newdp[j - 1])
            dp = newdp
        return dp[n - 1]

    def longestPalindromeSubseq_3(self, s):
        """
        :type s: str
        :rtype: int
        1319ms
        """
        # if s==s[::-1]:
        #     return len(s)
        l = len(s)
        self.dp=[[1 for j in range(l)] for i in range(l)]
        for i in range(0,l-1)[::-1]:
            for j in range(i+1,l):
                # print((i,i+length))
                if s[i]==s[j]:
                    if i+1<=j-1:
                        a=self.dp[i+1][j-1]
                    else:
                        a=0
                    self.dp[i][j]=a+2
                else:
                    a = self.dp[i + 1][j]
                    b = self.dp[i][j - 1]
                    self.dp[i][j] = max(self.dp[i][j], a, b)
                # print(self.dp)
        return self.dp[0][-1]

# print(Solution().longestPalindromeSubseq_1('qweksweaafgaaesss'))
# print(Solution().longestPalindromeSubseq_1("cbbd"))
# print(Solution().longestPalindromeSubseq_1("aa"))
# print(Solution().longestPalindromeSubseq_1("aaaaa"))
# print(Solution().longestPalindromeSubseq_1("ab"))
# print(Solution().longestPalindromeSubseq_1("abcscbaxyzs"))
print(Solution().longestPalindromeSubseq_3("a"*1000))




