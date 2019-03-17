"""
We have a grid of 1s and 0s; the 1s in a cell represent bricks.  A brick will not drop if and only if it is directly connected to the top of the grid, or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially. Each time we want to do the erasure at the location (i, j), the brick (if it exists) on that location will disappear, and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input:
grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
Output: [2]
Explanation:
If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.

Example 2:
Input:
grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
Output: [0,0]
Explanation:
When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move. So each erasure will cause no bricks dropping.  Note that the erased brick (1, 0) will not be counted as a dropped brick.



Note:

    The number of rows and columns in the grid will be in the range [1, 200].
    The number of erasures will not exceed the area of the grid.
    It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
    An erasure may refer to a location with no brick - if it does, no bricks drop.


"""
import numpy as np
class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        466ms
        """
        m, n = len(grid), len(grid[0])
        # 先把所有会遇到的地方标记出来，如果原本在该位置有brick的标记为0，否则标记为-1
        for hit in hits:
            grid[hit[0]][hit[1]] = 0 if grid[hit[0]][hit[1]] == 1 else -1
        # 从(i, j)出发所有能到达的位置
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and grid[i][j] == 1):
                return 0
            grid[i][j] = 2
            count = 1
            count += dfs(i - 1, j)
            count += dfs(i, j + 1)
            count += dfs(i + 1, j)
            count += dfs(i, j - 1)
            return count
        # 把所有最后都不会落下的brick标记为2
        for i in range(n):
            dfs(0, i)
        # 判断(i, j)是不是和顶部相连
        def is_connect(i, j):
            if i == 0:
                return True
            if i - 1 >= 0 and grid[i - 1][j] == 2:
                return True
            if i + 1< m and grid[i + 1][j] == 2:
                return True
            if j - 1 >= 0 and grid[i][j - 1] == 2:
                return True
            if j + 1 < n and grid[i][j + 1] == 2:
                return True
            return False
        result = [0] * len(hits)

        for i in reversed(range(len(hits))):
            hit = hits[i]
            # 如果这个位置原本就不存在brick，恢复为0（因为没有重复位置，所以可以恢复）
            if grid[hit[0]][hit[1]] == -1:
                grid[hit[0]][hit[1]] = 0
                continue
            # 如果不和现存的brick相连，则说明该位置在这次hit之前就消失了，恢复为1
            grid[hit[0]][hit[1]] = 1
            if not is_connect(hit[0], hit[1]):
                continue
            # 否则计算这块联动几块，扣除自身
            # print(np.array(grid))
            # grid[hit[0]][hit[1]] = 1
            result[i] += dfs(hit[0], hit[1]) - 1

        return result

    def hitBricks_1(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """

        m, n = len(grid), len(grid[0])

        # Connect unconnected bricks and
        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            ret = 1
            grid[i][j] = 2
            ret += dfs(i - 1, j)
            ret += dfs(i + 1, j)
            ret += dfs(i, j - 1)
            ret += dfs(i, j + 1)
            return ret

        # Check whether (i, j) is connected to Not Falling Bricks
        def is_connected(i, j):
            ret = False
            ret |= (h[0] - 1 >= 0 and grid[h[0] - 1][h[1]] == 2)
            ret |= (h[0] + 1 < m and grid[h[0] + 1][h[1]] == 2)
            ret |= (h[1] - 1 >= 0 and grid[h[0]][h[1] - 1] == 2)
            ret |= (h[1] + 1 < n and grid[h[0]][h[1] + 1] == 2)
            ret |= (h[0] == 0)
            return ret

        # Mark whether there is a brick at the each hit
        for h in hits:
            if grid[h[0]][h[1]] == 1:
                grid[h[0]][h[1]] = 0
            else:
                grid[h[0]][h[1]] = -1

        # Get grid after all hits
        for i in range(n):
            dfs(0, i)

        # Reversely add the block of each hits and get count of newly add bricks
        ret = [0] * len(hits)
        for i in reversed(range(len(hits))):
            h = hits[i]
            if grid[h[0]][h[1]] == -1:
                continue
            grid[h[0]][h[1]] = 1
            if not is_connected(h[0], h[1]):
                continue
            ret[i] = dfs(h[0], h[1]) - 1

        return ret
print(Solution().hitBricks([[1,0,0,0,0,0], [1,1,1,1,0,0], [1,0,0,1,0,0], [1,0,0,1,1,0], [0,0,0,0,0,0]],
                           [[1, 0],[2, 2],[1, 3]]))
