"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string S.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

Example 2:
Input: "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.

Example 3:
Input: "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]

Example 4:
Input: "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.

Note:

    4 <= S.length <= 12.
    S[0] = "(", S[S.length - 1] = ")", and the other elements in S are digits.

"""
class Solution(object):
    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        106ms
        """
        def all_struct(s):
            if len(s) == 1:
                return [s]
            if s[0] == '0' and s[-1] == '0':
                return []
            elif s[0] == '0':
                a = s[0] + '.' + s[1:]
                return [a]
            elif s[-1] == '0':
                return [s]
            else:
                A = [s]
                for i in range(1, len(s)):
                    a = s[:i] + '.' + s[i:]
                    A.append(a)
                return A

        l = len(S) - 1
        C = []
        for i in range(2, l):
            A = all_struct(S[1:i])
            B = all_struct(S[i:-1])
            # print(A,B)
            if A != [] and B != []:
                for a in A:
                    for b in B:
                        C.append('(' + a + ', ' + b + ')')
        return C
print(Solution().ambiguousCoordinates("(123)"))
print(Solution().ambiguousCoordinates("(00011)"))
print(Solution().ambiguousCoordinates("(0123)"))
print(Solution().ambiguousCoordinates("(100)"))

