"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""


class MyCalendar(object):
    """
    1729ms
    """
    def __init__(self):
        self.book_1 = [[-float('inf'), -float('inf')], [float('inf'), float('inf')]]

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        s = self.book_1
        l = len(s) - 1
        start_1 = 0
        while start_1 < l:
            if s[start_1][1] <= start and end <= s[start_1 + 1][0]:
                self.book_1.insert(start_1 + 1, [start, end])
                return True
            elif s[start_1][1] > end:
                break
            start_1 += 1
        return False





        # Your MyCalendar object will be instantiated and called as such:
        # obj = MyCalendar()
        # param_1 = obj.book(start,end)
obj = MyCalendar()
param_1 = obj.book(10,20)
print(param_1)
param_1 = obj.book(15,25)
print(param_1)
param_1 = obj.book(20,30)
print(param_1)

import bisect


class MyCalendar(object):
    """
    238ms
    """
    def __init__(self):
        self.time = []
        self.hs = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.time) == 0:
            self.time.append(start)
            self.hs[start] = end
            return True

        x = bisect.bisect_left(self.time, start)
        if x == 0:
            if end > self.time[x]:
                return False
        elif x == len(self.time):
            if start < self.hs[self.time[x - 1]]:
                return False
        else:
            if start < self.hs[self.time[x - 1]] or end > self.time[x]:
                return False
        self.hs[start] = end
        bisect.insort(self.time, start)
        return True
