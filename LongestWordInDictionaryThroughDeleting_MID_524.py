"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output:
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        685ms
        """
        def isSubsequence(str1, str2):
            if len(str1) < len(str2):
                return False
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

        lists = sorted(d, key = lambda k:len(k), reverse = True)
        result = []
        for l in lists:
            if isSubsequence(s, l):
                if result == [] or len(result[-1]) == len(l):
                    result.append(l)
                else:
                    break
            if result != [] and len(result[-1]) > len(l):
                break
        if len(result) <= 0:
            return ''
        return sorted(result)[0]

    def findLongestWord_1(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        115ms
        """
        d.sort(key=lambda x: (-len(x), x))
        d.append('')
        S = len(s)

        def isSubsequence(t):
            i = 0
            for c in t:
                i = s.find(c, i) + 1
                if i <= 0:
                    return False
            return True

        return next(x for x in d if isSubsequence(x))

    def findLongestWord_3(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        669ms
        """
        def isSubsequence(str1, str2):
            if len(str1) < len(str2):
                return False
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

        lists = sorted(d, key = lambda k:(-len(k), k))

        for l in lists:
            if isSubsequence(s, l):
                    return l
        return ''

s = "abpcplea"
d = ["ale","apple","monkey","plea",'abpcp']
print(Solution().findLongestWord_3(s, d))

s = "apple"
d = ["zxc","vbn"]
print(Solution().findLongestWord(s, d))