"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]

"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        36ms
        """
        if len(s)==0:
            return s
        if k>len(s):
            return s[::-1]
        mins=len(s)//k+1
        s1=''
        for i in range(mins):
            a = min(len(s), (i + 1) * k)
            tmp=s[k*i:a]
            if i%2==0:
                s1+=tmp[::-1]
            else:
                s1+=tmp
        return s1

print(Solution().reverseStr('abcdefg',2))