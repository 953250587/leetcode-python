"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        179ms
        """
        self.l=len(grid)
        if self.l<=0:
            return 0
        self.r=len(grid[0])
        area=[[0 for i in range(self.r)] for i in range(self.l)]
        self.count=0
        self.max=0

        def area_find(i, j):
            if grid[i][j] != 1 or area[i][j] != 0:
                return
            area[i][j] = 1
            self.count+=1
            if i-1>=0:
                area_find(i-1,j)
            if j-1>=0:
                area_find(i,j-1)
            if i+1<self.l:
                area_find(i+1,j)
            if j+1<self.r:
                area_find(i,j+1)

        for i in range(self.l):
            for j in range(self.r):
                if area[i][j]==0 and grid[i][j]==1:
                    area_find(i,j)
                    self.max=max(self.max,self.count)
                    self.count=0
                else:
                    area[i][j]=-1
        return self.max
grid=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# grid=[[0,0,0,0,0,0,0,0]]
print(Solution().maxAreaOfIsland(grid))
