"""
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
class Solution:
    def repeatedStringMatch_1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        206ms
        """
        times = -(-len(B) // len(A))  # Equal to ceil(len(b) / len(a))
        for i in range(2):
            if B in (A * (times + i)):
                return times + i
        return -1
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        499ms
        """
        al=len(A)
        bl=len(B)
        if bl<=al:
            if len(A.replace(B,''))!=al:
                return 1
            elif len((A*2).replace(B,''))!=2*al:
                return 2
            else:
                return -1
        else:
            d=(bl%al>0)
            # print(d)
            c=bl//al+d
            if len((A*(c)).replace(B,''))!=c*al:
                return c
            elif len((A*(c+1)).replace(B,''))!=(c+1)*al:
                return c+1
            else:
                return -1



# print(Solution().repeatedStringMatch("abcd","cdabcdabc"))
# print(Solution().repeatedStringMatch("abcd","da"))
# print(Solution().repeatedStringMatch("a","aa"))
print(Solution().repeatedStringMatch("abc","aabcbabcc"))
