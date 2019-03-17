"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.

Notes:

    3 <= points.length <= 50.
    No points will be duplicated.
     -50 <= points[i][j] <= 50.
    Answers within 10^-6 of the true value will be accepted as correct.

"""


class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        441ms
        """
        import math
        def LENGTH_2(a):
            return a[0] ** 2 + a[1] ** 2
        ans = 0
        l = len(points)
        for i in range(l - 2):
            for j in range(i, l - 1):
                for k in range(j, l):
                    a = [points[i][0] - points[k][0], points[i][1] - points[k][1]]
                    b = [points[j][0] - points[k][0], points[j][1] - points[k][1]]
                    c = a[0] * b[0] + a[1] * b[1]
                    ans = max(ans, math.sqrt(LENGTH_2(a) * LENGTH_2(b) - c ** 2))
        return ans / 2.0

    def largestTriangleArea_1(self, p):
        """
        :type points: List[List[int]]
        :rtype: float
        158ms
        """
        import itertools
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1, p2, p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)

        return max(f(a, b, c) for a, b, c in itertools.combinations(p, 3))
print(Solution().largestTriangleArea(points = [[0,0],[0,1],[1,0],[0,2],[2,0]]))
print(Solution().largestTriangleArea([[8,10],[2,7],[9,2],[4,10]]))
