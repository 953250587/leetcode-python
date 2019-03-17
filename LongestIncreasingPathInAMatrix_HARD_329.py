"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        732ms
        """
        m = len(matrix)
        if m <= 0:
            return 0
        n = len(matrix[0])
        self.dicts = {}
        self.max = 0
        self.max_list = None
        def dfs(i, j):
            if (i, j) in self.dicts:
                return self.dicts[(i, j)]
            lists = [[0, 1], [1, 0], [0, -1],[-1, 0]]
            s_max = 1
            # s_max_list = [matrix[i][j]]
            for dic in lists:
                new_i = i + dic[0]
                new_j = j + dic[1]
                if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n:
                    if matrix[new_i][new_j] > matrix[i][j]:
                        a = dfs(new_i, new_j)
                        if a + 1 > s_max:
                            s_max = a + 1
                            # s_max_list = [matrix[i][j]] + a
            self.dicts[(i, j)] = s_max
            return s_max

        for i in range(m):
            for j in range(n):
                a = dfs(i, j)
                if a > self.max:
                    self.max = a
                    # self.max_list = a
        return self.max

    def longestIncreasingPath_1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        466ms
        """
        if not matrix:
            return 0
        row = len(matrix);
        col = len(matrix[0])

        cach = [[0] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                self.DSF(matrix, i, j, row, col, cach)
        return max(map(max, cach))

    def DSF(self, matrix, i, j, row, col, cach):
        if cach[i][j]:
            return cach[i][j]
        cach[i][j] = 1
        neighbor = (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)
        for x, y in neighbor:
            if 0 <= x < row and 0 <= y < col and matrix[x][y] > matrix[i][j]:
                cach[i][j] = max(cach[i][j], 1 + self.DSF(matrix, x, y, row, col, cach))
        return cach[i][j]

    def longestIncreasingPath_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        252ms
        """
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for i in range(m)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                                   dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                                   dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                                   dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]

        return max(dfs(x, y) for x in range(m) for y in range(n))
nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(Solution().longestIncreasingPath(nums))

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
print(Solution().longestIncreasingPath(nums))


