"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:

    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].

"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        126ms
        """
        if len(s2) < len(s1):
            return False
        l = len(s1)
        if l <= 0:
            return True
        l2 = len(s2)

        b = [0] * 26
        for s in s1:
            b[ord(s) - ord('a')] += 1

        c = [0] * 26
        s3 = s2[0: l]
        for s in s3:
            c[ord(s) - ord('a')] += 1

        def isOk(b, c):
            for i in range(26):
                if b[i] - c[i] != 0:
                    return False
            return True

        if isOk(b, c):
            return True
        for i in range(l, l2):
            char = ord(s2[i]) - ord('a')
            char_befor = ord(s2[i - l]) - ord('a')
            c[char_befor] -= 1
            c[char] += 1
            if isOk(b, c):
                return True
        return False

    def checkInclusion_1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        99ms
        """

        l1 = len(s1)
        l2 = len(s2)

        if l1 > l2:
            return False

        dic = {}
        for x in s1:
            if x in dic:
                dic[x] += 1
            else:
                dic[x] = 1

        cnt = 0

        for i in range(l1):
            if s2[i] in dic:
                if dic[s2[i]] > 0:
                    cnt += 1
                dic[s2[i]] -= 1

        if cnt == l1:
            return True

        i = l1
        while i < l2:
            if s2[i] in dic:
                if dic[s2[i]] > 0:
                    cnt += 1
                dic[s2[i]] -= 1

            if s2[i - l1] in dic:
                if dic[s2[i - l1]] >= 0:
                    cnt -= 1
                dic[s2[i - l1]] += 1

            if cnt == l1:
                return True

            i += 1
        return False

    def checkInclusion_2(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        95ms
        """
        if not s1: return True
        if len(s2) < len(s1): return False

        m, n, a = len(s1), len(s2), ord('a')
        count = [0] * 26
        for c in s1:
            count[ord(c) - a] += 1
        for i in range(0, m):
            count[ord(s2[i]) - a] -= 1
        for i in range(m, n):
            if not any(count):
                return True
            count[ord(s2[i - m]) - a] += 1
            count[ord(s2[i]) - a] -= 1
        return not any(count)

s1 = "ab"
s2 = "eidbaooo"
print(Solution().checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(Solution().checkInclusion(s1, s2))