"""
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)



Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.



Note:

1 <= p <= 1000
0 <= q <= p

"""


class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        31 ms
        """
        def gcd(p, q):
            if q == 0:
                return p
            else:
                return gcd(q, p % q)
        a = gcd(p, q)
        t1 = q / a # p的个数
        t2 = p / a # q的个数
        print(t1, t2)
        if t1 % 2 == 0:
            return 0
        else:
            if t2 % 2 == 1:
                return 1
            else:
                return 2
print(Solution().mirrorReflection(p = 2, q = 1))
print(Solution().mirrorReflection(p = 3, q = 2))
print(Solution().mirrorReflection(3, 1))
print(Solution().mirrorReflection(5, 3))