"""
 Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
import numpy as np
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        242ms
        """
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    b = 0
                else:
                    b = 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + b)
        print(np.array(dp))

        return dp[-1][-1]

    def minDistance_1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        139ms
        """
        # d = [[0]*(len(word2)+1) for i in range(len(word1)+1)]
        # for i in range(1,len(word1)+1):
        #     d[i][0] = i
        # for j in range(1,len(word2)+1):
        #     d[0][j] = j
        # for i in range(1,len(word1)+1):
        #     for j in range(1,len(word2)+1):
        #         a = d[i-1][j] + 1
        #         b = d[i][j-1] + 1
        #         if word1[i-1] == word2[j-1]:
        #             c = d[i-1][j-1]
        #         else:
        #             c = d[i-1][j-1] + 1
        #         d[i][j] = min(a,b,c)
        # return d[len(word1)][len(word2)]
        dp = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j

        def edit_dist(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = edit_dist(i - 1, j - 1)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(edit_dist(i - 1, j - 1), edit_dist(i, j - 1), edit_dist(i - 1, j))
                return dp[i][j]

        return edit_dist(len(word1), len(word2))
print(Solution().minDistance('ad', 'abcd'))
print(Solution().minDistance('', '123'))
print(Solution().minDistance('123', ''))