"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]

Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import bisect
class SummaryRanges(object):
    """
    406ms
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.start = []
        self.end = []
        self.sets = set()

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.sets:
            return
        self.sets.add(val)
        if val + 1 in self.sets and val - 1 in self.sets:
            self.start.remove(val + 1)
            self.end.remove(val - 1)
        elif val + 1 in self.sets:
            pos_up = bisect.bisect_left(self.start, val + 1)
            self.start[pos_up] = val
        elif val - 1 in self.sets:
            pos_down = bisect.bisect_left(self.end, val - 1)
            self.end[pos_down] = val
        else:
            bisect.insort(self.start, val)
            bisect.insort(self.end, val)
        # print('up', self.start)
        # print('down', self.end)
    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        result = []
        for i in range(len(self.start)):
            result.append(Interval(self.start[i], self.end[i]))
        return result



        # Your SummaryRanges object will be instantiated and called as such:
        # obj = SummaryRanges()
        # obj.addNum(val)
        # param_2 = obj.getIntervals()
obj = SummaryRanges()
for num in [1, 3, 8, 2, 7, 5, 10]:
    obj.addNum(num)
    a = obj.getIntervals()
    for k in a:
        print([k.start, k.end])
    print('***********', num)

obj = SummaryRanges()
for num in [1, 3, 7, 2, 6, 9, 4, 10, 5]:
    obj.addNum(num)
    a = obj.getIntervals()
    for k in a:
        print([k.start, k.end])
    print('***********', num)


class SummaryRanges(object):
    """
    382ms
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.interval = []
        self.reg = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        self.reg.append(val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        while (self.reg != []):
            self.cur = self.reg.pop(0)
            if self.interval == []:
                self.interval.append(Interval(self.cur, self.cur))
                continue
            if self.interval[0].start > self.cur:
                if self.interval[0].start - 1 == self.cur:
                    self.interval[0].start = self.cur
                else:
                    self.interval.insert(0, Interval(self.cur, self.cur))
                continue
            if self.interval[-1].end < self.cur:
                if self.interval[-1].end + 1 == self.cur:
                    self.interval[-1].end = self.cur
                else:
                    self.interval.append(Interval(self.cur, self.cur))
                continue

            pre = -1
            l = 0
            r = len(self.interval) - 1
            while (l < r):
                mid = (l + r) / 2
                if self.interval[mid].end >= self.cur:
                    r = mid
                elif self.interval[mid + 1].start <= self.cur:
                    l = mid + 1
                else:
                    pre = mid
                    break

            if pre != -1:
                if self.interval[pre].end == self.cur - 1 and self.interval[pre + 1].start == self.cur + 1:
                    self.interval[pre].end = self.interval[pre + 1].end
                    del self.interval[pre + 1]
                elif self.interval[pre].end != self.cur - 1 and self.interval[pre + 1].start == self.cur + 1:
                    self.interval[pre + 1].start = self.cur
                elif self.interval[pre].end == self.cur - 1 and self.interval[pre + 1].start != self.cur + 1:
                    self.interval[pre].end = self.cur
                else:
                    self.interval.insert(pre + 1, Interval(self.cur, self.cur))
        return self.interval