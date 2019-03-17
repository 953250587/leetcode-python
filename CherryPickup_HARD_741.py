"""
 In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:

Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

Example 1:

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation:
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Note:
grid is an N by N 2D array, with 1 <= N <= 50.
Each grid[i][j] is an integer in the set {-1, 0, 1}.
It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""
import numpy as np
class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        992ms
        """
        n = len(grid)
        if n <= 0:
            return 0
        if n == 1:
            return grid[0][0]
        self.dp = [[-1] * n for _ in range(n)]
        self.dp[0][0] = grid[0][0]

        for step in range(1, 2 * n - 1):
            curr = [[-1] * n for _ in range(n)]
            for i in range(max(step - n + 1, 0), min(step + 1, n)):
                for j in range(max(step - n + 1, 0), min(step + 1, n)):
                    if grid[i][step - i] == -1 or grid[j][step - j] == -1:
                        continue
                    cherry = self.dp[i][j]
                    if i > 0:
                        cherry = max(cherry, self.dp[i - 1][j])
                    if j > 0:
                        cherry = max(cherry, self.dp[i][j - 1])
                    if i > 0  and j > 0:
                        cherry = max(cherry, self.dp[i - 1][j - 1])
                    if cherry < 0:
                        continue
                    if i != j:
                        curr[i][j] = cherry + grid[i][step - i] + grid[j][step - j]
                    else:
                        curr[i][j] = cherry + grid[i][step - i]
            self.dp = curr

        return max(self.dp[-1][-1], 0)




grid = [[0, 1, -1],[1, 0, -1],[1, 1,  1]]
grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
print(Solution().cherryPickup(grid))

grid = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
print(Solution().cherryPickup(grid))

grid = [[1,-1,-1,-1,-1],[1,0,1,-1,-1],[0,-1,1,0,1],[1,0,1,1,0],[-1,-1,-1,1,1]]
print(Solution().cherryPickup(grid))




