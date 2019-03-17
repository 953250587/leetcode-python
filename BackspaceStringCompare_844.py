"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.



Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".


Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
"""


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
         54 ms
        """
        def new_str(S):
            s = []
            for char in S:
                if char != '#':
                    s.append(char)
                else:
                    if s:
                        s.pop()
            s = ''.join(s)
            return s
        return new_str(S) == new_str(T)
print(Solution().backspaceCompare( S = "ab#c", T = "ad#c"))
print(Solution().backspaceCompare( S = "ab##", T = "c#d#"))
print(Solution().backspaceCompare(  S = "a##c", T = "#a#c"))
print(Solution().backspaceCompare( S = "a#c", T = "b"))
