"""
There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        209ms
        """
        new_list=sorted(points,key=lambda point:(point[0],point[1]))
        print(new_list)
        if len(new_list)<=0:
            return 0
        end=new_list[0][1]
        count=1
        for i in new_list[1:]:
            if i[0]<=end:
                end=min(end,i[1])
                continue
            else:
                count+=1
                end=i[1]
        return count

    def findMinArrowShots_1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        122ms
        """
        if len(points) == 0:
            return 0
        points = sorted(points, key=lambda point: point[1])
        arrowpos = points[0][1]
        count = 1
        for point in points[1:]:
            if arrowpos >= point[0]:
                continue
            arrowpos = point[1]
            count += 1
        return count

points=[[7,8], [2,8], [1,6], [7,10],[9,11],[9,13]]
print(Solution().findMinArrowShots(points))

points=[[10,16], [2,8], [1,6], [7,12]]
print(Solution().findMinArrowShots(points))

points=[[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(Solution().findMinArrowShots(points))