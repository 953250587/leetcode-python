"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

    All the input integers are in the range [-10000, 10000].
    A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    Input points have no order.


"""
class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        42ms
        """
        points = [p1, p2, p3, p4]
        s = sorted(points, key = lambda a:(a[0], a[1]))
        def pow(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        a = pow(s[0], s[1])
        b = pow(s[1], s[3])
        c = pow(s[3], s[2])
        d = pow(s[2], s[0])

        f = pow(s[1], s[2])
        g = pow(s[0], s[3])

        if a == b == c == d and f == g and a != 0:
            return True
        else:
            return False

    def validSquare_1(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        39ms
        """
        p = [p1, p2, p3, p4]
        dic = {}
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                s = self.helper(p[i], p[j])
                dic[s] = dic.get(s, 0) + 1

        return len(dic) == 2 and 2 in dic.values() and 4 in dic.values()

    def helper(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
p1 = [0,0]
p2 = [0,0]
p3 = [0,0]
p4 = [0,0]
print(Solution().validSquare(p1, p2, p3, p4))

p1 = [0,0]
p2 = [1,1]
p3 = [1,-1]
p4 = [2,0]
print(Solution().validSquare(p1, p2, p3, p4))

p1 = [0,0]
p2 = [3,4]
p3 = [4,-3]
p4 = [7,1]
print(Solution().validSquare(p1, p2, p3, p4))

p1 = [1,1]
p2 = [5,3]
p3 = [3,5]
p4 = [7,7]
print(Solution().validSquare(p1, p2, p3, p4))