"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.



Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""


class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        2028 ms
        """
        import collections
        dicts_row = collections.defaultdict(set)
        # dicts_column = collections.defaultdict(set)

        for point in points:
            dicts_row[point[0]].add(point[1])  # 竖线
            # dicts_column[point[1]].add(point[0])  # 横线
        l = len(points)
        min_val = float('inf')
        for i in range(l - 1):
            for j in range(i + 1, l):
                # 确认为对角线上的两个点
                if points[i][0] != points[j][0] and points[i][1] != points[j][1]:
                    # 判断能否构成矩形
                    if points[j][1] in dicts_row[points[i][0]] and points[i][1] in dicts_row[points[j][0]]:
                        min_val = min(min_val, abs(points[i][0] - points[j][0]) * abs(points[i][1] - points[j][1]))
        return min_val if min_val != float('inf') else 0

    def minAreaRect_1(self, points):
        """
        112ms
        :param points:
        :return:
        """
        import collections
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0


print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))

