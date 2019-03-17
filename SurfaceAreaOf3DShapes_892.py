"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50
"""


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        68 ms
        """
        l = len(grid)
        r = len(grid[0])

        def count(i, j):
            a = 0
            dics = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for dic in dics:
                i_1 = i + dic[0]
                j_1 = j + dic[1]
                if 0 <= i_1 < l and 0 <= j_1 < r:
                    a += max(0, grid[i][j] - grid[i_1][j_1])
                else:
                    a += grid[i][j]
            return a
        ans = 0
        for i in range(l):
            for j in range(r):
                ans += count(i, j)
                if grid[i][j] != 0:
                    ans += 2
        return ans
print(Solution().surfaceArea([[2]]))
print(Solution().surfaceArea([[1,2],[3,4]]))
print(Solution().surfaceArea([[1,0],[0,2]]))
print(Solution().surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))
