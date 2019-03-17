"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""


class Solution(object):
    def __init__(self, w):
        """
        :type w: List[int]
         276 ms
        """
        self.max_proportion = sum(w)
        self.Lists = []
        start = 0.1
        for x in w:
            start += x
            self.Lists.append(start)


    def pickIndex(self):
        """
        :rtype: int
        """
        import bisect
        import random
        a = random.randint(1, self.max_proportion)
        b = bisect.bisect(self.Lists, a)

        return b




        # Your Solution object will be instantiated and called as such:
        # obj = Solution(w)
        # param_1 = obj.pickIndex()


import random


class Solution_1(object):
    def __init__(self, w):
        """
        :type w: List[int]
        176ms
        """
        self.sums = []
        for weight in w:
            if not self.sums:
                self.sums.append(weight)
            else:
                self.sums.append(weight + self.sums[-1])

    def pickIndex(self):
        """
        :rtype: int
        """
        import bisect

        pick = random.uniform(0, self.sums[-1])
        return bisect.bisect_left(self.sums, pick)