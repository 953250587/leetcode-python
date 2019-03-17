"""
A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

    sx, sy, tx, ty will all be integers in the range [1, 10^9].


"""


class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        37ms
        """
        while tx >= sx and ty >= sy and tx > 0 and ty > 0:
            if tx == sx and ty == sy:
                return True
            if tx == ty:
                return False
            elif tx > ty:
                tx -= max((tx - sx) // ty, 1) * ty
            else:
                ty -= max((ty - sy) // tx, 1) * tx
            # print(tx, ty)

        return False
# print(Solution().reachingPoints(sx = 1, sy = 1, tx = 3, ty = 5))
print(Solution().reachingPoints(sx = 1, sy = 1, tx = 2, ty = 2))
# print(Solution().reachingPoints(sx = 1, sy = 1, tx = 1, ty = 1))
print(Solution().reachingPoints(35, 13, 455955547, 420098884))
print(Solution().reachingPoints(3,3,12,9))