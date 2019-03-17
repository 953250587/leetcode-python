"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR".
Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

Note:

    1 <= len(start) = len(end) <= 10000.
    Both start and end will only consist of characters in {'L', 'R', 'X'}.

"""


class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        77MS
        """
        l = len(start)
        stack_R = []
        stack_L = []
        i = 0
        while i < l:
            if start[i] == 'R':
                if end[i] != 'R':
                    stack_R.append('R')
            elif start[i] == 'L':
                if end[i] != 'L':
                    if not stack_R and stack_L and stack_L[-1] == 'L':
                        stack_L.pop()
                    else:
                        return False
            if end[i] == 'R':
                if start[i] != 'R':
                    if not stack_L and stack_R and stack_R[-1] == 'R':
                        stack_R.pop()
                    else:
                        return False
            elif end[i] == 'L':
                if start[i] != 'L':
                    stack_L.append('L')
            # print(stack, i)
            i += 1
        return True if not (stack_L or stack_R) else False

    def canTransform_1(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        107MS
        """

        def rx(s):
            return ''.join(s.split('X'))

        def plc(s):
            al = []
            ar = []
            for i, c in enumerate(s):
                if c == 'L':
                    al.append(i)
                elif c == 'R':
                    ar.append(i)
            return [al, ar]

        if rx(start) != rx(end):
            return False
        sl, sr = plc(start)
        el, er = plc(end)
        for i in range(len(sl)):
            if el[i] > sl[i]:
                return False
        for i in range(len(sr)):
            if er[i] < sr[i]:
                return False
        return True


print(Solution().canTransform(start = "RXXLRXRXL", end = "XRLXXRRLX"))
print(Solution().canTransform("XXRXXLXXXX", "XXXXRXXLXX"))
print(Solution().canTransform('RL', 'LR'))
