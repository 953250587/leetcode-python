"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.



Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false


Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""


class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        60 ms
        """
        if len(A) != len(B):
            return False
        count = 0
        charsA = [0 for _ in range(26)]
        charsB = [0 for _ in range(26)]
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
            charsA[ord(A[i]) - ord('a')] += 1
            charsB[ord(B[i]) - ord('a')] += 1
        if (count == 2 and all([charsA[i] == charsB[i] for i in range(26)])) \
                or (count == 0 and any([i > 1 for i in charsA])):
            return True
        else:
            return False

    def buddyStrings_1(self, A, B):
        """
        38ms
        :param A:
        :param B:
        :return:
        """
        if len(A) != len(B): return False
        if A == B and len(set(A)) < len(A): return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]
print(Solution().buddyStrings( A = "ab", B = "ba"))
print(Solution().buddyStrings( A = "ab", B = "ab"))
print(Solution().buddyStrings( A = "aa", B = "aa"))
print(Solution().buddyStrings( A = "aaaaaaabc", B = "aaaaaaacb"))
print(Solution().buddyStrings( A = "", B = "aa"))
print(Solution().buddyStrings('ab', 'ca'))