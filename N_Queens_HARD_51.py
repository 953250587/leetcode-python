"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""
import numpy as np
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        92ms
        """
        self.n = n
        row = [-1] * n
        sets = {i for i in range(n)}
        result = []
        def dfs(row_count, sets):
            if row_count >= self.n:
                self.ans = []
                for val in row:
                    s1 = '.' * (val)
                    s2 = '.' * (n - val - 1)
                    self.ans.append(s1 + 'Q' + s2)
                result.append(self.ans)
            a = list(sets)
            for i in a:
                row[row_count] = i
                flag = True
                for k in range(row_count):
                    if abs(k - row_count) == abs(row[k] - i):
                        flag = False
                        break
                if flag:
                    sets.remove(i)
                    dfs(row_count + 1, sets)
                    sets.add(i)
        dfs(0, sets)
        return result

    def solveNQueens_1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        65ms
        """

        def next_queen(queens, n, xydif, xysum):
            row = len(queens)
            if row == n:
                res.append(queens)
                return
            for col in range(n):
                if col not in queens:
                    if (col - row) not in xydif and (col + row) not in xysum:
                        next_queen(queens + [col], n, xydif + [col - row], xysum + [col + row])

        if n == 1:
            return [['Q']]
        res = []
        configs = []
        for col in range(n // 2):
            next_queen([col], n, [col], [col])

        for queens in res:
            config = []
            for q in queens:
                config.append('.' * q + 'Q' + '.' * (n - 1 - q))
            configs.append(config)
            configs.append([row[::-1] for row in config])

        res = []
        if n % 2:
            col = n // 2
            next_queen([col], n, [col], [col])
        for queens in res:
            config = []
            for q in queens:
                config.append('.' * q + 'Q' + '.' * (n - 1 - q))
            configs.append(config)

        return configs



a = Solution().solveNQueens(4)
for i in a:
    print(np.array(i))


