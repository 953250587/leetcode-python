"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
         43 ms
        """
        def isMagic(i, j):
            s = set()
            for x in range(3):
                for y in range(3):
                    s.add(grid[i + x][j + y])
            if len(s) == 9 and max(s) == 9 and min(s) == 1:
                a = sum([grid[i + x][j + x] for x in range(3)])
                b = sum([grid[i + (2 - x)][j + x] for x in range(3)])
                if a != b:
                    return False
                for k in range(3):
                    row = sum([grid[i + k][j + y] for y in range(3)])
                    column = sum([grid[i + x][j + k] for x in range(3)])
                    if a == row == column:
                        continue
                    else:
                        return False
                return True
            else:
                return False

        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if i + 3 <= m and j + 3 <= n:
                    if isMagic(i, j):
                        ans += 1
        return ans

    def numMagicSquaresInside_1(self, g):
        """
        36ms
        :param g:
        :return:
        """
        def isMagic(i, j):
            s = "".join(str(g[i + x / 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3])
            return g[i][j] % 2 == 0 and (s in "43816729" * 2 or s in "43816729"[::-1] * 2)

        return sum(isMagic(i, j) for i in range(len(g) - 2) for j in range(len(g[0]) - 2) if g[i + 1][j + 1] == 5)
print(Solution().numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]]))
