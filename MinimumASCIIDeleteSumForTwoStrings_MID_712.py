"""
Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].
"""
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        802MS
        """
        dp, s1_ascii, s2_ascii, f = [[0 for i in range(len(s2) + 1)] for j in range(len(s1) + 1)], 0, 0, 0
        for i in range(1, len(s1) + 1):
            s1_ascii += ord(s1[i - 1])
            for j in range(1, len(s2) + 1):
                if not f: s2_ascii += ord(s2[j - 1])
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            f = 1
        return s1_ascii + s2_ascii - 2 * dp[i][j]

    def minimumDeleteSum_1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        458MS
        """
        s1 = [ord(ch) for ch in s1]
        s2 = [ord(ch) for ch in s2]
        dp = [0] * (len(s2) + 1)
        for ch in s1:
            temp = dp[:]
            for i in range(1, len(s2) + 1):
                if ch == s2[i - 1]:
                    temp[i] = dp[i - 1] + ch
                else:
                    temp[i] = max(temp[i - 1], dp[i])
            dp = temp
        return sum(s1) + sum(s2) - 2 * dp[-1]

