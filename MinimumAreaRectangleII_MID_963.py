"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.



Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.


Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        overtime
        """
        """
        https: // blog.csdn.net / qq_17550379 / article / details / 85234090
        判断4个点到中点的距离是否一致即可判断矩形！！
        """
        # combinations 用于求序列的组合,permutations 用于生成一个排列
        from itertools import combinations, permutations

        # 判断是否为矩形
        def isRectangle(p1, p2, p3, p4):
            def _dis(p1, p2):
                return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            x_c = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
            y_c = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
            d1 = _dis(p1, (x_c, y_c))
            d2 = _dis(p2, (x_c, y_c))
            d3 = _dis(p3, (x_c, y_c))
            d4 = _dis(p4, (x_c, y_c))
            return d1 == d2 and d1 == d3 and d1 == d4

        # 计算矩形面积
        def calcRectangleArea(p1, p2, p3, p4):
            # 计算直角
            def _isOrthogonal(p1, p2, p3):
                return (p2[0] - p1[0]) * (p2[0] - p3[0]) + (p2[1] - p1[1]) * (p2[1] - p3[1]) == 0
            # 任取一个直角
            for three_point in permutations((p1, p2, p3, p4), 3):
                if _isOrthogonal(*three_point):
                    p1, p2, p3 = three_point
                    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5 * \
                           ((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2) ** 0.5

        min_value = float('inf')
        for points in combinations(points, 4):
            if isRectangle(*points):
                min_value = min(min_value, calcRectangleArea(*points))
        return 0 if min_value == float('inf') else min_value


    def minAreaFreeRect_1(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        120 ms
        13.3 MB
        """
        from itertools import combinations
        from collections import defaultdict

        # 计算所有点之间的线段并且记录下来
        def distance(point_x, point_y):
            return ((point_x[0] - point_y[0]) ** 2 + (point_x[1] - point_y[1]) ** 2) ** 0.5

        # 判断两条线段是否中点相交
        def isMiddle(point_x2, point_y2):
            return ((point_x2[0][0] + point_x2[1][0]) / 2 == (point_y2[0][0] + point_y2[1][0]) / 2
                and (point_x2[0][1] + point_x2[1][1]) / 2 == (point_y2[0][1] + point_y2[1][1]) / 2)

        # 根据线段长度记录
        dicts_distance = defaultdict(list)
        for points2 in combinations(points, 2):
            points_distance = distance(*points2)
            dicts_distance[points_distance].append(points2)
        minArea = float("inf")
        for key in dicts_distance:
            if len(dicts_distance[key]) < 2:
                continue
            for points4 in combinations(dicts_distance[key], 2):
                if isMiddle(*points4):
                   p2 = points4[0][0]
                   p1, p3 = points4[1]
                   minArea = min(minArea, ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5 * \
                                          ((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2) ** 0.5)
        return 0 if minArea == float('inf') else minArea

    def minAreaFreeRect_2(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        84 ms
        12.4MB
        使用复数解法！！！完全没想过！！！！
        """
        import collections, itertools
        points = [complex(*z) for z in sorted(points)]
        seen = collections.defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            seen[Q - P].append((P + Q) / 2)

        ans = float("inf")
        for A, candidates in seen.iteritems():
            for P, Q in itertools.combinations(candidates, 2):
                if A.real * (P - Q).real == -A.imag * (P - Q).imag:
                    ans = min(ans, abs(A) * abs(P - Q))
        return ans if ans < float("inf") else 0





if __name__ == '__main__':
    print(Solution().minAreaFreeRect_1([[0,1],[2,1],[1,1],[1,0],[2,0]]))  # 1.0
    print(Solution().minAreaFreeRect_1([[0,3],[1,2],[3,1],[1,3],[2,1]]))  # 0
    print(Solution().minAreaFreeRect_1([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]))  # 2.0
    print(Solution().minAreaFreeRect_1([[4,0],[2,1],[3,4],[3,1],[2,0],[4,4],[1,1],[4,3],[2,2],[4,1],[0,1],[1,4],[0,2]]))  # 2.0



