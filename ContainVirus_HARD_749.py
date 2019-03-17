"""
 A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region -- the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night. There will never be a tie.

Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected, return the number of walls used.

Example 1:

Input: grid =
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:

Input: grid =
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

Example 3:

Input: grid =
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.

Note:

    The number of rows and columns of grid will each be in the range [1, 50].
    Each grid[i][j] will be either 0 or 1.
    Throughout the described process, there is always a contiguous viral region that will infect strictly more uncontaminated squares in the next round.

"""
import numpy as np
class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        238ms
        """
        self.grid = grid
        self.m = len(grid)
        if self.m <= 0:
            return 0
        self.n = len(grid[0])
        def dfs(i, j, marks):
            if self.grid[i][j] != 1:
                if self.grid[i][j] == 0:
                    self.count += 1
                    if self.mark[i][j] != -marks:
                        self.num += 1
                        self.mark[i][j] = -marks
                return
            if self.mark[i][j] != 0:
                return
            self.mark[i][j] = marks
            diract = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for dic in diract:
                new_i = i + dic[0]
                new_j = j + dic[1]
                if new_i >= 0 and new_i < self.m and new_j >= 0 and new_j < self.n:
                    dfs(new_i, new_j, marks)
        flag = True
        ans = 0
        while flag:
            flag = False
            self.max = [-1, -1, -1]
            self.mark = [[0] * self.n for _ in range(self.m)]
            marks = 0
            for i in range(self.m):
                for j in range(self.n):
                    if self.grid[i][j] == 1 and self.mark[i][j] == 0:
                        flag = True
                        marks += 1
                        self.num = 0
                        self.count = 0
                        dfs(i, j, marks)
                        if self.num > self.max[0]:
                            self.max[0] = self.num
                            self.max[1] = marks
                            self.max[2] = self.count
            if flag:
                ans += self.max[2]
            for i in range(self.m):
                for j in range(self.n):
                    if self.mark[i][j] != self.max[1] and self.mark[i][j] > 0:
                        diract = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                        for dic in diract:
                            new_i = i + dic[0]
                            new_j = j + dic[1]
                            if new_i >= 0 and new_i < self.m and new_j >= 0 and new_j < self.n:
                                self.grid[new_i][new_j] = max(1, self.grid[new_i][new_j])
                    elif self.mark[i][j] == self.max[1]:
                        self.grid[i][j] = 2
            # print(np.array(self.mark))
            # print(np.array(self.grid))
            # print(self.max)
            # print(ans)
        return ans

#
grid = [[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
print(Solution().containVirus(grid))

grid = [[1,1,1],
 [1,0,1],
 [1,1,1]]
print(Solution().containVirus(grid))

grid = [[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
print(Solution().containVirus(grid))

grid = [[1]]
print(Solution().containVirus(grid))

grid = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,1,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
print(Solution().containVirus(grid))


grid = [[0,0,1,1,1,0,1,0,0,0],
        [1,1,1,0,0,0,1,1,0,1],
        [0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,1,0,1,0,0,0],
        [1,0,0,0,1,1,1,0,0,0],
        [0,0,0,1,0,1,1,0,0,0],
        [1,0,0,0,0,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1],
        [0,1,0,0,0,0,0,0,1,0],
        [1,1,0,0,0,1,0,1,0,0]]
print(Solution().containVirus(grid))

grid = [[0,1,0,1,1,1,1,1,1,0],
        [0,0,0,1,0,0,0,0,0,0],
        [0,0,1,1,1,0,0,0,1,0],
        [0,0,0,1,1,0,0,1,1,0],
        [0,1,0,0,1,0,1,1,0,1],
        [0,0,0,1,0,1,0,1,1,1],
        [0,1,0,0,1,0,0,1,1,0],
        [0,1,0,1,0,0,0,1,1,0],
        [0,1,1,0,0,1,1,0,0,1],
        [1,0,1,1,0,1,0,1,0,1]]
print(Solution().containVirus(grid))

grid = [[1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0],[1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,1,0,0],[1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1],[1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1],[1,1,1,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1],[0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,1,0,1,0],[1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1],[1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,1,0,1,0,0],[1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,1],[1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1],[1,0,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1],[1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,1,1,1],[1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,1,0,1],[1,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,0,1],[0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0],[1,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,0,0,0],[0,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1],[1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1],[0,0,1,1,1,1,1,1,0,1,0,0,1,0,0,0,0,1,1,1],[0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0]]
print(Solution().containVirus(grid))