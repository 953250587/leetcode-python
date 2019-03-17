"""
A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.

queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.

removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).

Example 1:

addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)

Note:
A half open interval [left, right) denotes all real numbers left <= x < right.
0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
The total number of calls to addRange in a single test case is at most 1000.
The total number of calls to queryRange in a single test case is at most 5000.
The total number of calls to removeRange in a single test case is at most 1000.
"""

import bisect
class RangeModule(object):

    def __init__(self):
        """
         593 ms
         """
        self.recom = []

    def bisect_insort(self, list, t):
        low, high = 0, len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            if list[mid][0] <= t:
                low = mid + 1
            elif list[mid][0] > t:
                high = mid - 1
            # else:
            #     return mid
        return low

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        recom = self.recom
        i = self.bisect_insort(recom, left)
        j = self.bisect_insort(recom, right)
        # print(i, j)
        if i == j:
            if i - 1 < 0 or (i - 1 >= 0 and recom[i - 1][1] < left):
                bisect.insort_left(recom, [left, right])
            else:
                recom[i - 1][1] = max(recom[i - 1][1], right)
        else:
            r = max(recom[j - 1][1], right)
            if i - 1 < 0 or (i - 1 >= 0 and recom[i - 1][1] < left):
                l = left
                s = i
            else:
                l = recom[i - 1][0]
                s = i - 1
            recom[s:j] = [[l, r]]




    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        recom = self.recom
        i = self.bisect_insort(recom, left)
        i -= 1
        if i >= 0 and recom[i][0] <= left and recom[i][1] >= right:
            return True
        return False

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        recom = self.recom
        i = self.bisect_insort(recom, left)
        print('i', i)
        if i - 1 >= 0 and recom[i - 1][1] > right:
            end = recom[i - 1][1]
            recom[i - 1][1] = left
            bisect.insort_left(recom, [right, end])
        else:
            if i - 1 >= 0 and recom[i - 1][1] >= left:
                recom[i - 1][1] = left
            while i < len(recom) and recom[i][1] <= right:
                recom.pop(i)
            if i < len(recom):
                recom[i][0] = max(recom[i][0], right)




        # Your RangeModule object will be instantiated and called as such:
        # obj = RangeModule()
        # obj.addRange(left,right)
        # param_2 = obj.queryRange(left,right)
        # obj.removeRange(left,right)
# obj = RangeModule()
# obj.addRange(1,3)
# print(obj.recom)
# obj.addRange(6,8)
# print(obj.recom)
# obj.addRange(-2, -1)
# print(obj.recom)
# obj.addRange(3,4)
# print(obj.recom)
# obj.addRange(0,7)
# print(obj.recom)

obj = RangeModule()
# obj.addRange(10,20)
# print(obj.recom)
# obj.addRange(21,30)
# print(obj.recom)
# obj.addRange(0,15)
# print(obj.recom)
# obj.addRange(30,50)
# print(obj.recom)
# obj.removeRange(22,35)
# print(obj.recom)
# obj.removeRange(12,38)
# print(obj.recom)
# print(obj.queryRange(10,14))
# print(obj.recom)
# print(obj.queryRange(13,15))
# print(obj.recom)
# print(obj.queryRange(16,17))
# print(obj.recom)

# a = ["RangeModule","queryRange","queryRange","addRange","addRange","queryRange","queryRange","queryRange","removeRange","addRange","removeRange","addRange","removeRange","removeRange","queryRange","queryRange","queryRange","queryRange","removeRange","addRange","removeRange","queryRange","addRange","addRange","removeRange","queryRange","removeRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange","queryRange","queryRange","addRange","removeRange","addRange","addRange","addRange","queryRange","removeRange","addRange","queryRange","addRange","queryRange","removeRange","removeRange","addRange","addRange","queryRange","queryRange","addRange","addRange","removeRange","removeRange","removeRange","queryRange","removeRange","removeRange","addRange","queryRange","removeRange","addRange","addRange","queryRange","removeRange","queryRange","addRange","addRange","addRange","addRange","addRange","removeRange","removeRange","addRange","queryRange","queryRange","removeRange","removeRange","removeRange","addRange","queryRange","removeRange","queryRange","addRange","removeRange","removeRange","queryRange"]
# b = [[],[21,34],[27,87],[44,53],[69,89],[23,26],[80,84],[11,12],[86,91],[87,94],[34,52],[1,59],[62,96],[34,83],[11,59],[59,79],[1,13],[21,23],[9,61],[17,21],[4,8],[19,25],[71,98],[23,94],[58,95],[12,78],[46,47],[50,70],[84,91],[51,63],[26,64],[38,87],[41,84],[19,21],[18,56],[23,39],[29,95],[79,100],[76,82],[37,55],[30,97],[1,36],[18,96],[45,86],[74,92],[27,78],[31,35],[87,91],[37,84],[26,57],[65,87],[76,91],[37,77],[18,66],[22,97],[2,91],[82,98],[41,46],[6,78],[44,80],[90,94],[37,88],[75,90],[23,37],[18,80],[92,93],[3,80],[68,86],[68,92],[52,91],[43,53],[36,37],[60,74],[4,9],[44,80],[85,93],[56,83],[9,26],[59,64],[16,66],[29,36],[51,96],[56,80],[13,87],[42,72],[6,56],[24,53],[43,71],[36,83],[15,45],[10,48]]
# for i in range(1, len(a)):
#     print(a[i], b[i])
#     if a[i] == 'queryRange':
#         print(obj.queryRange(b[i][0], b[i][1]))
#     elif a[i] == 'addRange':
#         obj.addRange(b[i][0], b[i][1])
#         print(obj.recom)
#     else:
#         obj.removeRange(b[i][0], b[i][1])
#         print(obj.recom)

a =['', "addRange","removeRange","queryRange","queryRange"]
b = [[], [14,100],[1,8],[77,80],[8,43]]
for i in range(1, len(a)):
    print(a[i], b[i])
    if a[i] == 'queryRange':
        print(obj.queryRange(b[i][0], b[i][1]))
    elif a[i] == 'addRange':
        obj.addRange(b[i][0], b[i][1])
        print(obj.recom)
    else:
        obj.removeRange(b[i][0], b[i][1])
        print(obj.recom)


from bisect import bisect_left, bisect_right

class RangeModule(object):

    def __init__(self):
        """
        510ms
        """
        self.range = [-float('inf'), float('inf')]

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        li = bisect_left(self.range, left)
        ri = bisect_right(self.range, right)
        if li % 2 == 0:
            li = li - 1
            left = self.range[li]
        if ri % 2 == 0:
            right = self.range[ri]
            ri += 1
        self.range[li:ri] = [left, right]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        li = bisect_right(self.range, left)
        ri = bisect_left(self.range, right)
        return li == ri and li % 2 == 0

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        li = bisect_left(self.range, left)
        ri = bisect_right(self.range, right)
        if li % 2 == 1:
            li = li - 1
            left = self.range[li]
        if ri % 2 == 1:
            right = self.range[ri]
            ri += 1
        self.range[li:ri] = [left, right]