"""
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:

Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:

Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them.

Note:

    All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
    All input integers will range from 0 to 100.
    The garden has at least one tree.
    All coordinates are distinct.
    Input points have NO order. No order required for output.

"""
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        451MS
        """
        l = len(points)
        new_points = sorted(points, key=lambda a:(a.x, -a.y))
        begin = new_points[0].x
        end = new_points[-1].x
        print([[i.x, i.y] for i in new_points])
        result = set()
        for point in new_points:
            if point.x == end or point.x == begin:
                result.add(point)
        start = new_points[0]
        result.add(start)
        i = 1
        while i < l:
            if new_points[i].x == end:
                break
            max_k = -float('inf')
            max_k_pos = -1
            for j in range(i, l):
                point = new_points[j]
                if point.x != start.x:
                    cur_k = (point.y - start.y) / (point.x - start.x)
                    if cur_k > max_k:
                        max_k = cur_k
                        max_k_pos = j
            start = new_points[max_k_pos]
            result.add(start)
            i = max_k_pos + 1

        new_points = sorted(points, key=lambda a: (a.x, a.y))
        start = new_points[0]
        result.add(start)
        i = 1
        while i < l:
            if new_points[i].x == end:
                break
            min_k = float('inf')
            min_k_pos = -1
            for j in range(i, l):
                point = new_points[j]
                if point.x != start.x:
                    cur_k = (point.y - start.y) / (point.x - start.x)
                    if cur_k < min_k:
                        min_k = cur_k
                        min_k_pos = j
            start = new_points[min_k_pos]
            result.add(start)
            i = min_k_pos + 1
        return list(result)

    def outerTrees_1(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        271MS
        """
        # looks like the problem of searching the convex hull...
        # ok, it is. but i still need to see the AM algorithm...

        # sort the points accoridng to the x coordinates
        sorted_points = sorted(points, key=lambda p: (p.x, p.y))

        # prepare a helper function to define clockwise rotation
        def cross_product(origin, pnt1, pnt2):
            # cross product of OA, OB
            return (pnt1.x - origin.x) * (pnt2.y - origin.y) - (pnt1.y - origin.y) * (pnt2.x - origin.x)

        # now lets construct the upper hull
        upper_hull = []
        for pnt in sorted_points:
            while len(upper_hull) > 1 and cross_product(pnt, upper_hull[-2], upper_hull[-1]) < 0:
                upper_hull.pop()
            upper_hull.append(pnt)
        # lower_hull
        lower_hull = []
        for pnt in sorted_points[::-1]:
            while len(lower_hull) > 1 and cross_product(pnt, lower_hull[-2], lower_hull[-1]) < 0:
                lower_hull.pop()
            lower_hull.append(pnt)
        return list(set(upper_hull + lower_hull))
L = [[8,3],[9,8],[2,6],[8,7],[9,9]]
points = []
for i in L:
    points.append(Point(i[0], i[1]))
a =Solution().outerTrees(points)
print(sorted([[i.x, i.y]for i in a], key=lambda a:(a[0], -a[1])))

# L = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# points = []
# for i in L:
#     points.append(Point(i[0], i[1]))
# a =Solution().outerTrees(points)
# print(sorted([[i.x, i.y]for i in a], key=lambda a:(a[0], -a[1])))
#
#
# L = [[1,2],[2,2],[4,2]]
# points = []
# for i in L:
#     points.append(Point(i[0], i[1]))
# a =Solution().outerTrees(points)
# print(sorted([[i.x, i.y]for i in a], key=lambda a:(a[0], -a[1])))
#
# L = [[3,0],[4,0],[5,0],[6,1],[7,2],[7,3],[7,4],[6,5],[5,5],[4,5],[3,5],[2,5],[1,4],[1,3],[1,2],[2,1],[4,2],[0,3]]
# points = []
# for i in L:
#     points.append(Point(i[0], i[1]))
# a =Solution().outerTrees(points)
# print(sorted([[i.x, i.y]for i in a], key=lambda a:(a[0], -a[1])))

# L = [[0,0],[0,100],[100,100],[100,0],[50,50]]
# points = []
# for i in L:
#     points.append(Point(i[0], i[1]))
# a =Solution().outerTrees(points)
# print(sorted([[i.x, i.y]for i in a], key=lambda a:(a[0], -a[1])))


import math


class Solution:
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        251MS
        """

        def area(a, b, c):
            return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)

        if len(points) <= 3:
            return points

        points.sort(key=lambda p: (p.x, p.y))

        stack = []
        for point in points:
            while len(stack) >= 2 and area(stack[-2], stack[-1], point) < 0:
                stack.pop()
            stack.append(point)

        results = set(stack)

        stack = []
        for point in reversed(points):
            while len(stack) >= 2 and area(stack[-2], stack[-1], point) < 0:
                stack.pop()
            stack.append(point)

        results |= set(stack)

        return list(results)

