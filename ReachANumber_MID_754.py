"""
 You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

Note:
target will be a non-zero integer in the range [-10^9, 10^9].
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        36ms
        """
        import math
        if target < 0:
            return self.reachNumber(-target)
        if target == 0:
            return 0
        # if target == 1:
        #     return 1
        # if target == 2:
        #     return 3
        m = math.floor(math.sqrt(2 * target))
        a = m * (m + 1)
        if a < 2 * target:
            m = m + 1
        a = m * (m + 1) // 2
        # print(a)
        while (a - target) % 2 == 1:
            m += 1
            a += m
        return int(m)

# print(Solution().reachNumber(3))
# print(Solution().reachNumber(2))
# print(Solution().reachNumber(4))
print(Solution().reachNumber(1))
print(Solution().reachNumber(2))
print(Solution().reachNumber(3))
print(Solution().reachNumber(5))
print(Solution().reachNumber(7))
print(Solution().reachNumber(18))
print(Solution().reachNumber(9))
print(Solution().reachNumber(12))