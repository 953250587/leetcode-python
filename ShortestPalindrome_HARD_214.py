"""
 Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        def getnext(a, next):
            al = len(a)
            next[0] = -1
            k = -1
            j = 0
            while j < al - 1:
                if k == -1 or a[j] == a[k]:
                    j += 1
                    k += 1
                    if a[j] == a[k]:
                        next[j] = next[k]
                    else:
                        next[j] = k
                else:
                    k = next[k]

        b = s
        next = [0] * len(b)
        getnext(b, next)
        print(next)

        self.nums = 0
        def KmpSearch(a, b):
            i = j = 0
            al = len(a)
            bl = len(b)
            while i < al and j < bl:
                if j == -1 or a[i] == b[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]
            self.nums = j

        KmpSearch(s[::-1], s)
        print(self.nums)
        return s[self.nums:][::-1] + s

    def shortestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        52ms
        """
        size = len(s)
        while True:
            start = 0
            end = size - 1
            while end >= 0:
                if s[start] == s[end]:
                    start += 1
                end -= 1
            if start == size:
                return s[size:][::-1] + s
            size = start

    def shortestPalindrome_2(self, s):
        """
        :type s: str
        :rtype: str
        42ms
        """
        if len(s) <= 1:
            return s
        maxj, c = 1, 0
        while c <= len(s) / 2:
            i = j = c
            while j + 1 < len(s) and s[j + 1] == s[j]:
                j += 1
            if i > len(s) - j - 1:
                break
            c = j + 1
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            if i < 0:
                maxj = max(maxj, j)
        return s[maxj:][::-1] + s
print(Solution().shortestPalindrome("aacecaaa"))
# print(Solution().shortestPalindrome("abcd"))
print(Solution().shortestPalindrome("aabba"))
print(Solution().shortestPalindrome("aabbaa"))