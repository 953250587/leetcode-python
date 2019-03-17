"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:

Input: ["23:59","00:00"]
Output: 1

Note:

    The number of time points in the given list is at least 2 and won't exceed 20000.
    The input time is legal and ranges from 00:00 to 23:59.

"""
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        219ms
        """
        so = sorted(timePoints, key = lambda a:(a.split(':')))
        start = so[0]
        self.min = 1500
        def calc_diff(time1, time2):
            h = int(time1[0:2]) - int(time2[0:2])
            min_1 = int(time1[-2:]) - int(time2[-2:])
            return h * 60 + min_1
        print(so)
        for i in so[1:]:
            self.min = min(self.min, calc_diff(i, start))
            start = i
        h = int(so[0][0:2]) + 24 - int(start[0:2])
        min_1 = int(so[0][-2:]) - int(start[-2:])
        self.min = min(self.min, h * 60 + min_1)
        return self.min

    def findMinDifference_1(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """

        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])

        minutes = map(convert, timePoints)
        minutes.sort()

        return min((y - x) % (24 * 60)
                   for x, y in zip(minutes, minutes[1:] + minutes[:1]))

    def findMinDifference_2(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        maxium = 1440
        # 用数组来代替sort
        total = [False for x in range(maxium)]

        for time in timePoints:
            hour, mi = time.split(":")
            if total[int(hour) * 60 + int(mi)] == True:
                return 0
            else:
                total[int(hour) * 60 + int(mi)] = True
        minimum = total
        prev = -1
        first = -1
        for n in range(0, len(total)):
            if total[n]:
                if prev != -1:
                    # 当前近还是绕一圈近
                    minimum = min(n - prev, maxium - (n - prev), minimum)
                else:
                    first = n
                prev = n
        return min(maxium - (prev - first), minimum)



timePoints = ["23:59", "00:00", '01:10', '02:48', '22:38', '22:23', '01:05']
print(Solution().findMinDifference(timePoints))