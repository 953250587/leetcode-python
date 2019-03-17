"""
Given a list of non-overlapping axis-aligned rectangles rects, write a function pick which randomly and uniformily picks an integer point in the space covered by the rectangles.

Note:

An integer point is a point that has integer coordinates.
A point on the perimeter of a rectangle is included in the space covered by the rectangles.
ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer coordinates of the bottom-left corner, and [x2, y2] are the integer coordinates of the top-right corner.
length and width of each rectangle does not exceed 2000.
1 <= rects.length <= 100
pick return a point as an array of integer coordinates [p_x, p_y]
pick is called at most 10000 times.
Example 1:

Input:
["Solution","pick","pick","pick"]
[[[[1,1,5,5]]],[],[],[]]
Output:
[null,[4,1],[4,1],[3,3]]
Example 2:

Input:
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
Output:
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array of rectangles rects. pick has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

import random
class Solution(object):
    def __init__(self, rects):
        """
        :type w: List[int]
         268 ms
        """
        self.rects = rects
        self.sums = []
        for w in rects:
            weight = (w[2] - w[0] + 1) * (w[3] - w[1] + 1)
            if not self.sums:
                self.sums.append(weight)
            else:
                self.sums.append(weight + self.sums[-1])

    def pick(self):
        """
        :rtype: int
        """
        import bisect

        pick = random.uniform(0, self.sums[-1])
        b = bisect.bisect_left(self.sums, pick)

        x = random.randint(self.rects[b][0], self.rects[b][2])
        y = random.randint(self.rects[b][1], self.rects[b][3])
        return [x, y]


from bisect import bisect
from random import randint

class Solution_1(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        256ms
        """
        self.a=[0]
        for i in range(len(rects)-1):
            self.a.append(self.a[-1]+(rects[i][2]-rects[i][0]+1)*(rects[i][3]-rects[i][1]+1))
            rects[i]=[rects[i][0],rects[i][1],rects[i][2]-rects[i][0]+1]
        self.b,self.k=rects,self.a[-1]+(rects[-1][2]-rects[-1][0]+1)*(rects[-1][3]-rects[-1][1]+1)-1
        self.b[-1]=[self.b[-1][0],self.b[-1][1],self.b[-1][2]-self.b[-1][0]+1]

    def pick(self):
        """
        :rtype: List[int]
        """
        n=randint(0,self.k)
        i=bisect(self.a,n)-1
        n-=self.a[i]
        return [n%self.b[i][2]+self.b[i][0],n//self.b[i][2]+self.b[i][1]]