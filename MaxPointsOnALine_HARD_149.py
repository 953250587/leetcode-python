"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        289ms
        """
        def gcd(a, b):
            a = abs(a)
            b = abs(b)
            if a < b:
                a, b = b, a
            if a % b == 0:
                return b
            else:
                return gcd(b, a % b)

        if points == []:
            return 0
        import collections
        max_1 = 1
        sets = set()
        l = len(points)
        dict_dup = {}
        for i in range(l - 1):
            dict_line = collections.defaultdict(int)
            flag = False
            if points[i] in dict_dup:
                dup = dict_dup[points[i]]
            else:
                dup = 1
                flag = True
            for j in range(i + 1, l):
                if flag and points[i].x == points[j].x and points[i].y == points[j].y:
                    dup += 1
                key = None
                if points[i].x == points[j].x and points[i].y != points[j].y:
                    a = (points[i].x) / 1.0
                    key = ('Y', a)
                elif points[i].x != points[j].x:
                    y = points[j].y - points[i].y
                    x = points[j].x - points[i].x
                    if y != 0:
                        g = gcd(y, x)
                        y //= g
                        x //= g
                        if x * y < 0:
                            k = '-' + str(abs(y)) + '/' + str(abs(x))
                        else:
                            k = str(abs(y)) + '/' + str(abs(x))
                    else:
                        k = str(y) + '/' + '0'
                    # k = (points[j].y - points[i].y) / (points[j].x - points[i].x) / 1.0
                    b_y = points[i].y * x - y * points[i].x
                    b_x = x
                    if b_y != 0:
                        b_g = gcd(b_y, b_x)
                        b_y //= b_g
                        b_x //= b_g
                        if b_x * b_y < 0:
                            b = '-' + str(abs(b_y)) + '/' + str(abs(b_x))
                        else:
                            b = str(abs(b_y)) + '/' + str(abs(b_x))
                    else:
                        b = str(b_y) + '/' + '0'
                    # b = (points[i].y - k * points[i].x) / 1.0
                    key = (k, b)
                if key and key not in sets:
                    dict_line[key] += 1
                print(i, j, key, dup, dict_line[key])
            if flag:
                dict_dup[points[i]] = dup
            for key in dict_line:
                max_1 = max(max_1, dict_line[key] + dup)
                sets.add(key)
            max_1 = max(max_1, dup)
        print(dict_dup)
        print(dict_line)
        return max_1

# point = [[1.1, 1.1], [2.2, 2.2], [2.2, 3],[2.2, 4], [2.2, 6], [2, 1], [3, 2], [4, 3]]
# points = []
# for i in point:
#     points.append(Point(i[0], i[1]))
# print(Solution().maxPoints(points))
#

point = [[0,0],[1,0],[0,0]]
points = []
for i in point:
    points.append(Point(i[0], i[1]))
print(Solution().maxPoints(points))

point = [[0,0],[1,0]]
points = []
for i in point:
    points.append(Point(i[0], i[1]))
print(Solution().maxPoints(points))
#
point = [[0,0],[94911151,94911150],[94911152,94911151]]
points = []
for i in point:
    points.append(Point(i[0], i[1]))
print(Solution().maxPoints(points))

point = [[2,3],[3,3],[-5,3]]
points = []
for i in point:
    points.append(Point(i[0], i[1]))
print(Solution().maxPoints(points))

import itertools
import fractions
import math
import collections


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        86ms
        """
        result = 0
        for i, p1 in enumerate(points):
            counts = collections.defaultdict(int)
            counts['max_int'] = 1
            #
            j = 0
            same = 0
            for j, p2 in enumerate(itertools.islice(points, i)):
                p2 = points[j]
                dx, dy = p2.x - p1.x, p2.y - p1.y

                if dx == 0 and dy == 0:
                    same += 1
                    continue
                elif dx == 0:
                    slope = 'max_int'
                else:
                    slope = dy / dx

                if slope not in counts:
                    counts[slope] = 1
                counts[slope] += 1

            local_max = same + max(counts.values())
            result = max(result, local_max)
        return result