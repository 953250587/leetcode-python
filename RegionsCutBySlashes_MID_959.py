"""
In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.



Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:



Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
"""


class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        376 ms
        """
        l = len(grid)
        memo = set()
        # 把原始1x1的矩阵由/和\\分成四块，顺时针记为1,2,3,4，根据不同分法有不同的连通性，然后dfs就可以了
        def dfs(i, j, pos):
            if (i, j, pos) in memo:
                return
            memo.add((i, j, pos))
            if grid[i][j] == '/':
                # 1和4联通
                if pos == 1 or pos == 4:
                    if i - 1 >= 0:
                        dfs(i - 1, j, 3)
                    if j - 1 >= 0:
                        dfs(i, j - 1, 2)
                    memo.add((i, j, 1))
                    memo.add((i, j, 4))
                # 2和3联通
                else:
                    if j + 1 < l:
                        dfs(i, j + 1, 4)
                    if i + 1 < l:
                        dfs(i + 1, j, 1)
                    memo.add((i, j, 2))
                    memo.add((i, j, 3))
            elif grid[i][j] == '\\':
                # 1和2联通
                if pos == 1 or pos == 2:
                    if i - 1 >= 0:
                        dfs(i - 1, j, 3)
                    if j + 1 < l:
                        dfs(i, j + 1, 4)
                    memo.add((i, j, 1))
                    memo.add((i, j, 2))
                # 3和4联通
                else:
                    if j - 1 >= 0:
                        dfs(i, j - 1, 2)
                    if i + 1 < l:
                        dfs(i + 1, j, 1)
                    memo.add((i, j, 3))
                    memo.add((i, j, 4))
            else:
                # 全部都联通
                if i - 1 >= 0:
                    dfs(i - 1, j, 3)
                if j - 1 >= 0:
                    dfs(i, j - 1, 2)
                if j + 1 < l:
                    dfs(i, j + 1, 4)
                if i + 1 < l:
                    dfs(i + 1, j, 1)
                for k in range(1, 5):
                    memo.add((i, j, k))
            return

        ans = 0
        # print(l)
        for i in range(l):
            for j in range(l):
                for pos in range(1, 5):
                    if (i, j, pos) not in memo:
                        # print(i, j, pos)
                        dfs(i, j, pos)
                        ans += 1
        return ans

    def regionsBySlashes_1(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        84ms
        """
        n = len(grid)
        res = [[[-1, -1] for _ in range(n)] for __ in range(n)]
        ic = [0]
        for i in range(n):
            for j in range(n):
                if res[i][j][0] >= 0 and res[i][j][1] >= 0:
                    continue
                self.mark(n, grid, res, i, j, ic, 0)
        return ic[0]

    def mark(self, n, grid, res, i, j, ic, direct):
        # dfs
        # print(res)
        # print(i, j, ic, direct)
        if not self.isValid(i, j, n):
            return
        if grid[i][j] == "/":
            if direct == 0:
                if res[i][j][0] < 0:
                    res[i][j][0] = ic[0]
                    self.mark(n, grid, res, i, j - 1, ic, 3)
                    self.mark(n, grid, res, i - 1, j, ic, 4)
                    ic[0] += 1
                if res[i][j][1] < 0:
                    res[i][j][1] = ic[0]
                    self.mark(n, grid, res, i, j + 1, ic, 1)
                    self.mark(n, grid, res, i + 1, j, ic, 2)
                    ic[0] += 1
            elif direct == 1:
                if res[i][j][0] < 0:
                    res[i][j][0] = ic[0]
                    self.mark(n, grid, res, i - 1, j, ic, 4)
            elif direct == 2:
                if res[i][j][0] < 0:
                    res[i][j][0] = ic[0]
                    self.mark(n, grid, res, i, j - 1, ic, 3)
            elif direct == 3:
                if res[i][j][1] < 0:
                    res[i][j][1] = ic[0]
                    self.mark(n, grid, res, i + 1, j, ic, 2)
            elif direct == 4:
                if res[i][j][1] < 0:
                    res[i][j][1] = ic[0]
                    self.mark(n, grid, res, i, j + 1, ic, 1)
        elif grid[i][j] == "\\":
            if direct == 0:
                if res[i][j][0] < 0:
                    res[i][j][0] = ic[0]
                    self.mark(n, grid, res, i, j - 1, ic, 3)
                    self.mark(n, grid, res, i + 1, j, ic, 2)
                    ic[0] += 1
                if res[i][j][1] < 0:
                    res[i][j][1] = ic[0]
                    self.mark(n, grid, res, i, j + 1, ic, 1)
                    self.mark(n, grid, res, i - 1, j, ic, 4)
                    ic[0] += 1
            elif direct == 1:
                if res[i][j][0] < 0:
                    res[i][j][0] = ic[0]
                    self.mark(n, grid, res, i + 1, j, ic, 2)
            elif direct == 2:
                if res[i][j][1] < 0:
                    res[i][j][1] = ic[0]
                    self.mark(n, grid, res, i, j + 1, ic, 1)
            elif direct == 3:
                if res[i][j][1] < 0:
                    res[i][j][1] = ic[0]
                    self.mark(n, grid, res, i - 1, j, ic, 4)
            elif direct == 4:
                if res[i][j][0] < 0:
                    res[i][j][0] = ic[0]
                    self.mark(n, grid, res, i, j - 1, ic, 3)
        else:
            if res[i][j][0] < 0:
                res[i][j][0] = ic[0]
                res[i][j][1] = ic[0]
                self.mark(n, grid, res, i, j - 1, ic, 3)
                self.mark(n, grid, res, i, j + 1, ic, 1)
                self.mark(n, grid, res, i - 1, j, ic, 4)
                self.mark(n, grid, res, i + 1, j, ic, 2)
                if direct == 0:
                    ic[0] += 1

    def isValid(self, i, j, n):
        return 0 <= i < n and 0 <= j < n

    def regionsBySlashes_2(self, grid):
        """
        296ms
        :param grid:
        :return:
        """
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))



# print(Solution().regionsBySlashes([" /",
#                                    "/ "
#                                    ]))
# print(Solution().regionsBySlashes([" /",
#                                    "  "
#                                    ]))
# print(Solution().regionsBySlashes(["\\/",
#                                    "/\\"
#                                    ]))
# print(Solution().regionsBySlashes(["/\\",
#                                    "\\/"
#                                    ]))
# print(Solution().regionsBySlashes([ "//",
#                                     "/ "
#                                    ]))
print(Solution().regionsBySlashes(["\\ \\ ",
                                   "\\/ /",
                                   "/\\\\\\",
                                   "\\ / "]))