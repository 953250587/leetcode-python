"""
Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""
from collections import defaultdict
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        35MS
        """
        self.dict = {}
        for str in strs:
            l =len(str)
            if l not in self.dict.keys():
                self.dict[l] = [str]
            else:
                self.dict[l].append(str)
        a = sorted(self.dict.items(), key = lambda k:k[0], reverse = True)
        print(a)

        def isSubsequence(str1, str2):
            if len(str1) < len(str2):
                str2, str1 = str1, str2
            start_j = -1
            for i in str2:
                start_j += 1
                while start_j < len(str1):
                    if str1[start_j] == i:
                        break
                    start_j += 1
                if start_j >= len(str1):
                    return False
            return True

        print(isSubsequence('ssbsgan', 'ssg'))
        print(isSubsequence('ssbsgan', 'abc'))

        self.list = []

        for item in a:
            for k in set(item[1]):
                num = item[1].count(k)
                if num > 1:
                    self.list.append(k)
                elif num == 1:
                    flag = True
                    for t in self.list:
                        if isSubsequence(k, t):
                            flag = False
                            break
                    if flag:
                        return len(k)
        return -1

    def findLUSlength_1(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        55ms
        """
        d = defaultdict(list)
        for s in strs:
            d[len(s)].append(s)

        longerStrs = []
        for i in range(10, -1, -1):
            if i not in d: continue
            for j, s1 in enumerate(d[i]):
                f = True
                for s2 in longerStrs + d[i][0:j] + d[i][j + 1:]:
                    if self.isSubsequence(s1, s2):
                        f = False
                        break
                if f:
                    return len(s1)
            longerStrs += d[i]

        return -1

    def isSubsequence(self, s1, s2):
        if len(s1) == len(s2):
            return s1 == s2
        elif len(s1) > len(s2):
            return False
        else:
            i = j = 0
            while i < len(s1) and j < len(s2):
                if s1[i] != s2[j]:
                    j += 1
                else:
                    i += 1
                    j += 1
            return i == len(s1)



strs = ["aba", "cdc", "eae"]
print(Solution().findLUSlength(strs))





a = 'ssbsgan'
b = 'ssg'
print(a in b)
