"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.



Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""


Note:

A.length == 4
0 <= A[i] <= 9
"""


class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        24 ms
        """
        import itertools
        t = itertools.permutations(A, 4)
        hour = -1
        min = -1
        for a in t:
            # print(a)
            temp_hour = a[0] * 10 + a[1]
            temp_min = a[2] * 10 + a[3]
            if 0 <= temp_hour <= 23 and 0 <= temp_min <= 59:
                if hour < temp_hour or (hour == temp_hour and min < temp_min):
                    hour = temp_hour
                    min = temp_min
        if hour == -1 or min == -1:
            return ''
        return '{:0>2}:{:0>2}'.format(str(hour), str(min))

    def largestTimeFromDigits_1(self, A):
        """
        :type A: List[int]
        :rtype: str
        20ms
        """
        import itertools
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            hours = 10 * h1 + h2
            mins = 10 * m1 + m2
            time = 60 * hours + mins
            if 0 <= hours < 24 and 0 <= mins < 60 and time > ans:
                ans = time

        return "{:02}:{:02}".format(*divmod(ans, 60)) if ans >= 0 else ""

print(Solution().largestTimeFromDigits([1,2,3,4]))
print(Solution().largestTimeFromDigits([5,5,5,5]))
print(Solution().largestTimeFromDigits([4,4,4,0]))
print(Solution().largestTimeFromDigits([0,0,0,0]))
print(Solution().largestTimeFromDigits([0,1,6,0]))
print(Solution().largestTimeFromDigits([1,9,6,0]))
print(Solution().largestTimeFromDigits([0,0,1,0]))
print(Solution().largestTimeFromDigits([2,0,6,6]))
