"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Example:

Input:
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2
Explanation:

Note:

    The width sum of bricks in different rows are the same and won't exceed INT_MAX.
    The number of bricks in each row is in range [1,10,000]. The height of wall is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.

"""

import bisect
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        l = len(wall)
        self.min = l
        if l <= 1 and len(wall[0]) <= 1:
            return 1
        elif l <= 1:
            return 0
        elif len(wall[0]) <= 1:
            return l
        r = sum(wall[0])
        a = {}
        keys = []
        mark = [1] * l
        for i in range(l):
            s = wall[i][0]
            if s != r:
                if s not in a.keys():
                    a[s] = [i]
                    bisect.insort_left(keys, s)
                else:
                    a[s].append(i)
        k_1 = 0
        while k_1 < len(keys):
            print(a)
            k = keys[k_1]
            lists = a[k]
            self.min = min(self.min, l - len(lists))
            for i in lists:
                s = wall[i][mark[i]] + k
                mark[i] += 1
                if s != r:
                    if s not in a.keys():
                        a[s] = [i]
                        bisect.insort_left(keys, s)
                    else:
                        a[s].append(i)
            k_1 +=1
        return self.min

    def leastBricks_1(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        78ms
        """
        import collections
        d = collections.defaultdict(int)
        for line in wall:
            i = 0
            for brick in line[:-1]:
                i += brick
                d[i] += 1
        # print len(wall), d
        return len(wall) - max(d.values() + [0])

    def leastBricks_2(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        78ms
        """
        import collections
        hm = collections.defaultdict(int)
        gap = 0
        for w in wall:
            gap = 0
            for l in w:
                gap += l
                hm[gap] += 1

        del hm[gap]

        return len(wall) - max(hm.values() if hm else [0])
# wall = [[1,2,2,1],
#  [3,1,2],
#  [1,3,2],
#  [2,4],
#  [3,1,2],
#  [1,3,1,1]]
# print(Solution().leastBricks(wall))
#
# wall = [[1]]
# print(Solution().leastBricks(wall))

wall = [[1,1],[2],[1,1]]
print(Solution().leastBricks(wall))
wall = [[1],[1],[1]]
print(Solution().leastBricks(wall))