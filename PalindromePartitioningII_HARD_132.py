"""
 Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


"""

import numpy as np
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        666ms
        """
        l = len(s)
        dp_is_palindrome = [[False] * l for _ in range(l)]
        dp_is_palindrome[0][0] = True
        for i in range(l):
            dp_is_palindrome[i][i] = True
            if s[i] == s[i - 1]:
                dp_is_palindrome[i - 1][i] = True
        for j in range(2, l):
            for i in range(0, j - 1):
                if s[i] == s[j] and dp_is_palindrome[i + 1][j - 1]:
                    dp_is_palindrome[i][j] = True
        print(np.array(dp_is_palindrome))
        dp = [l] * (l + 1)
        dp[0] = -1
        for i in range(l):
            for j in range(i + 1):
                if dp_is_palindrome[j][i]:
                    b = dp[j] + 1
                    dp[i + 1] = min(dp[i + 1], b)
        print(dp)
        return dp[-1]

    def minCut_1(self, s):
        """
        :type s: str
        :rtype: int
        326ms
        """
        size = len(s)
        cut = range(-1, size)
        for idx in range(1, size):
            for low, high in (idx, idx), (idx - 1, idx):
                while low >= 0 and high < size and s[low] == s[high]:
                    cut[high + 1] = min(cut[high + 1], cut[low] + 1)
                    low -= 1
                    high += 1
        return cut[-1]

    def minCut_2(self, s):
        """
        :type s: str
        :rtype: int
        38ms
        """
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2 + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]

    def minCut_3(self, s):
        """
        :type s: str
        :rtype: int
        242ms
        """
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]
print(Solution().minCut('aaabbaa'))
print(Solution().minCut('aab'))