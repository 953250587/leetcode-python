"""
 Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.

Note:
The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""

class MyCalendarTwo(object):

    def __init__(self):
        self.list = []
        self.dup = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        1189ms
        """
        if self.list == []:
            self.list.append([start, end])
            return True
        for i in self.dup:
            if (start < i[1] and start >= i[0]) or (end <= i[1] and end > i[0])\
                    or (start <= i[0] and end >= i[1]):
                return False
        print('d', self.dup)
        for i in self.list:
            if (start < i[1] and start >= i[0]):
                self.dup.append([start, min(i[1], end)])
            elif (end <= i[1] and end > i[0]):
                self.dup.append([max(i[0], start), end])
            elif (end >= i[1] and start <= i[0]):
                self.dup.append([i[0], i[1]])
        self.list.append([start, end])
        print('s', self.list)
        return True




# obj = MyCalendarTwo()
# print(obj.book(10, 20))
# print(obj.book(50, 60))
# print( obj.book(10, 40))
# print(obj.book(5, 15))
# print(obj.book(5, 10))
# print(obj.book(25, 55))

obj = MyCalendarTwo()
c = [[12,26],[70,85],[55,67],[2,13],[3,18],[91,100],[13,26],[17,27],[41,55],[15,26],[50,68],[34,52],[95,100],[23,33],[89,100],[27,43],[80,95],[97,100],[28,47],[45,58],[76,93],[56,75],[91,100],[61,77],[36,49],[18,32],[96,100],[96,100],[67,86],[46,64],[95,100],[17,35],[8,27],[4,14],[30,43],[74,89],[77,95],[98,100],[31,41],[35,53]]
for i in c:
    print(i[0], i[1])
    print(obj.book(i[0], i[1]))

# obj = MyCalendarTwo()
# print(obj.book(28, 46))
# print(obj.book(9, 21))
# print( obj.book(21, 39))
# print(obj.book(37, 48))
# print(obj.book(38, 50))
# print(obj.book(22, 39))
# print(obj.book(45, 50))
# print(obj.book(1, 12))
# print(obj.book(40, 50))
# print(obj.book(31, 44))




        # Your MyCalendarTwo object will be instantiated and called as such:
        # obj = MyCalendarTwo()
        # param_1 = obj.book(start,end)