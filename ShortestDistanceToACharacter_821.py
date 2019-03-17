"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]



Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.


"""


class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        64ms
        """
        import bisect
        a = []
        for i, char in enumerate(S):
            if char == C:
                a.append(i)
        result = []
        for i in range(len(S)):
            pos = bisect.bisect_left(a, i)
            if pos == 0:
                result.append(a[pos] - i)
            elif pos >= len(a):
                result.append(i - a[pos - 1])
            else:
                result.append(min(a[pos] - i, i - a[pos - 1]))

        return result

    def shortestToChar_1(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        101ms
        """
        n = len(S)
        res = [n] * n
        pos = -n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C: pos = i
            res[i] = min(res[i], abs(i - pos))
        return res
print(Solution().shortestToChar(S = "loveleetcode", C = 'e'))
print(Solution().shortestToChar("aaba","b"))