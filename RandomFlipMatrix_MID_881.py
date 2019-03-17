"""
You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix where all values are initially 0. Write a function flip which chooses a 0 value uniformly at random, changes it to 1, and then returns the position [row.id, col.id] of that value. Also, write a function reset which sets all values back to 0. Try to minimize the number of calls to system's Math.random() and optimize the time and space complexity.

Note:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows and 0 <= col.id < n_cols
flip will not be called when the matrix has no 0 values left.
the total number of calls to flip and reset will not exceed 1000.
Example 1:

Input:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
Output: [null,[0,1],[1,2],[1,0],[1,1]]
Example 2:

Input:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
Output: [null,[0,0],[0,1],null,[0,0]]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has two arguments, n_rows and n_cols. flip and reset have no arguments. Arguments are always wrapped with a list, even if there aren't any.
"""

import random
class Solution:

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n, self.m = n_rows, n_cols
        self.total = self.n * self.m - 1
        self.reset()

    def flip(self):
        """
        :rtype: List[int]
        """
        res = random.randint(0, self.total)
        while res in self.used:
            res = random.randint(0, self.total)
        self.used.add(res)
        return [res//self.m, res%self.m]

    def reset(self):
        """
        :rtype: void
        """
        self.used = set()



class Solution_1(object):

    def __init__(self, n_rows, n_cols):
        """
        :type n_rows: int
        :type n_cols: int
        """
        self.n_rows=n_rows
        self.n_cols=n_cols
        self.r_random=int(random.uniform(0,n_rows))
        self.c_random=int(random.uniform(0,n_cols))
        self.count=0
        self.s=set()
    def flip(self):
        """
        :rtype: List[int]
        """
        rvalue=(self.r_random+self.count)%self.n_rows
        cvalue=(self.c_random+self.count)%self.n_cols
        if (rvalue,cvalue) in self.s:
            self.r_random+=1
            rvalue=(self.r_random+self.count)%self.n_rows
            cvalue=(self.c_random+self.count)%self.n_cols
        self.s.add((rvalue,cvalue))
        self.count+=1

        return [rvalue,cvalue]

    def reset(self):
        """
        :rtype: void
        """
        self.r_random=int(random.uniform(0,self.n_rows))
        self.c_random=int(random.uniform(0,self.n_cols))
        self.count=0
        self.s.clear()
