"""
 Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        379ms
        """
        if s=='':
            return True
        if t=='':
            return False
        lt=len(t)
        ls=len(s)
        i_t=0
        i_s=0
        while i_t<lt:
            # print(t[i_t])
            if t[i_t]==s[i_s]:
                i_s+=1
            if i_s==ls:
                return True
            i_t+=1
        return False

    def isSubsequence_1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        45ms
        """
        idx = 0
        beg = 0

        while idx < len(s):

            if beg >= len(t):
                return False

            symbol = s[idx]
            pos = t.find(symbol, beg)

            if pos == -1:
                return False
            else:
                beg = pos + 1

            idx += 1

        return True
s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
s='a'
t=''
print(Solution().isSubsequence(s,t))