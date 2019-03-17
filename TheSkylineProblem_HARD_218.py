"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
Buildings Skyline Contour

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]

"""
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        106ms
        """
        import heapq
        events = sorted(buildings + [[b[1], float("inf"), 0] for b in buildings])
        skyline, curb = [], [(0, float("inf"))]
        for L, R, H in events:
            top = curb[0][0]
            while curb[0][1] <= L:
                heapq.heappop(curb)
            if H > 0:
                heapq.heappush(curb, (-H, R))
            if top != curb[0][0]:
                if skyline and L == skyline[-1][0]:
                    skyline[-1][1] = -curb[0][0]
                else:
                    skyline.append([L, -curb[0][0]])
        return skyline

    def getSkyline_1(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        82ms
        """
        cur = []
        ans = []
        if not buildings:
            return []
        now = buildings[0]
        ans.append([now[0], now[2]])
        # cur.append(now)
        for b in buildings[1:]:
            if b[0] > now[1]:
                cur.sort(key=lambda x: x[2])
                while cur:
                    if cur[-1][1] <= now[1]:
                        cur.pop()
                        continue

                    ans.append([now[1], cur[-1][2]])
                    if cur[-1][2] == now[2]:
                        ans.pop()
                    now = cur[-1]

                    if now[1] >= b[0]:
                        break
                    cur.pop()
                if not cur:
                    ans.append([now[1], 0])
                    now = b
                    ans.append([b[0], b[2]])
                else:
                    # cur.append(now)
                    if b[2] > now[2]:
                        cur.append(now)
                        now = b
                        ans.append([b[0], b[2]])
                        if cur[-1][2] == b[2]:
                            ans.pop()
                    else:
                        cur.append(b)
            else:
                if b[2] > now[2]:
                    cur.append(now)
                    now = b
                    if ans[-1][0] == b[0]:
                        ans.pop()
                    ans.append([b[0], b[2]])
                else:
                    cur.append(b)
        cur.sort(key=lambda x: x[2])
        while cur:
            if cur[-1][1] <= now[1]:
                cur.pop()
                continue
            ans.append([now[1], cur[-1][2]])
            if cur[-1][2] == now[2]:
                ans.pop()
            now = cur[-1]
            cur.pop()
        ans.append([now[1], 0])
        return ans




buildings = [ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]
print(Solution().getSkyline(buildings))


buildings = [[1,2,1],[1,2,2],[1,2,3]]
print(Solution().getSkyline(buildings))

buildings = [[1,3,1],[1,3,3],[1,3,2],[2,4,2]]
print(Solution().getSkyline(buildings))
#
buildings = [[2,13,10],[10,17,25],[12,20,14]]
print(Solution().getSkyline(buildings))