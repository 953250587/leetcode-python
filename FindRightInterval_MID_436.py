"""
 Given a set of intervals, for each of the interval i, check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i, which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index, which means that the interval j has the minimum start point to build the "right" relationship for interval i. If the interval j doesn't exist, store -1 for the interval i. Finally, you need output the stored value of each interval as an array.

Note:

    You may assume the interval's end point is always bigger than its start point.
    You may assume none of these intervals have the same start point.

Example 1:

Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.

Example 2:

Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.

Example 3:

Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.

"""
import bisect
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        275ms
        """
        self.dicts={}
        lists=[]
        for index, item in enumerate(intervals):
            self.dicts[item.start]=index
            lists.append(item.start)
        print(self.dicts)
        print(lists)
        lists=sorted(lists)
        result=[]
        for i in intervals:
            a=i.end
            if a>lists[-1]:
                result.append(-1)
            else:
                x_insert_point = bisect.bisect_left(lists, i.end)
                result.append(self.dicts[lists[x_insert_point]])
        return result

    def findRightInterval_1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        562ms
        """
        l = sorted((e.start, i) for i, e in enumerate(intervals))
        res = []
        for e in intervals:
            r = bisect.bisect_left(l, (e.end,))
            res.append(l[r][1] if r < len(l) else -1)
        return res
Input=[ [1,4], [2,3], [3,4] ]
a=[]
for i in Input:
    b=Interval(i[0],i[1])
    a.append(b)
print(Solution().findRightInterval(a))

Input=[ [3,4], [2,3], [1,2] ]
a=[]
for i in Input:
    b=Interval(i[0],i[1])
    a.append(b)
print(Solution().findRightInterval(a))

Input=[[1,2],[2,3],[0,1],[3,4]]
a=[]
for i in Input:
    b=Interval(i[0],i[1])
    a.append(b)
print(Solution().findRightInterval(a))

# L = [1,3,3,3,6,8,12,15]
# x = 7
# x_insert_point = bisect.bisect_left(L,x)
# print(x_insert_point)
# x_insert_point = bisect.bisect_right(L,x)
# print(x_insert_point)