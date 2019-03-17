"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false

Note:

    A and B will have length at most 100.


"""


class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        40ms
        """
        if A == B:
            return True
        dicts_A = []
        for i, char in enumerate(A):
            if char == B[0]:
                dicts_A.append(i)
        for i in dicts_A:
            if A[i:] + A[0:i] == B:
                return True
        return False

    def rotateString_1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        31ms
        """
        return len(A) == len(B) and B in A + A
print(Solution().rotateString(A = 'abcde', B = 'cdeab'))
print(Solution().rotateString(A = 'abcde', B = 'abced'))
