"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        54 ms
        """
        leaf_count, right_count = 0, 0
        start, end = 0, len(seats) - 1
        for i, seat in enumerate(seats):
            if seat == 0:
                leaf_count += 1
            else:
                start = i
                break
        for i in range(len(seats) - 1, -1, -1):
            if seats[i] == 0:
                right_count += 1
            else:
                end = i
                break
        middle_count = 0
        max_count = max(leaf_count, right_count)
        # print(start, end)
        for i in range(start + 1, end + 1):
            if seats[i] == 0:
                middle_count += 1
            else:
                max_count = max((middle_count + 1) // 2, max_count)
                middle_count = 0
            # print(middle_count)
        return max_count

    def maxDistToClosest_1(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        99ms
        """

        res = i = 0
        for index, val in enumerate(seats):
            if val == 1:
                res = i = index
                break
        j = i
        i += 1
        while i < len(seats):
            if seats[i] == 1:
                res = max(res, (i - j) // 2)
                j = i
            i += 1
        return max(res, len(seats) - j - 1)
print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
print(Solution().maxDistToClosest([1,0,0,0]))
print(Solution().maxDistToClosest([0,0,0,0,1,0,0,0]))
print(Solution().maxDistToClosest([1,0,0,0,1,0,0,0,0,0,0,1]))
