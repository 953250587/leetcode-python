"""
There is an m by n grid with a ball. Given the start coordinate (i,j) of the ball, you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right). However, you can at most move N times. Find out the number of paths to move the ball out of grid boundary. The answer may be very large, return it after mod 109 + 7.

Example 1:

Input:m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input:m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

Note:

    Once you move the ball out of boundary, you cannot move it back.
    The length and height of the grid is in range [1,50].
    N is in range [0,50].

"""
class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        192ms
        """
        self.moves = [ (-1, 0), (0, -1), (1, 0), (0, 1)]
        dests = [[0] * N for i in range(N)]
        self.DP = [[[-1] * N  for _ in range(n)] for _ in range(m)]
        self.K = N
        print(self.DP)
        # self.DP[i][j][0] = 1

        def dfs(i, j, k):
            sum_1 = 0
            if k < self.K:
                if self.DP[i][j][k] != -1:
                    return self.DP[i][j][k]
                for pos in self.moves:
                    x = i + pos[0]
                    y = j + pos[1]
                    if (x >= 0 and x < m) and (y >= 0 and y < n):
                        sum_1 += dfs(x, y, k + 1)
                        sum_1 %= 10 ** 9 + 7
                    else:
                        sum_1 += 1
                        sum_1 %= 10 ** 9 + 7
                self.DP[i][j][k] = sum_1
                print(k, self.DP)
                return sum_1
            else:
                return 0

        return dfs(i, j, 0)

        # print(self.DP)
        # return a

    def findPaths_1(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        115ms bfs
        """

        # Counts the total moves at each step
        def gen_new_tbl():
            return [[0] * n for _ in range(m)]

        curr_tbl = gen_new_tbl()
        next_tbl = gen_new_tbl()

        MOD = int(1e9 + 7)
        curr_tbl[i][j] = 1
        num_outs = 0
        for step in range(N):
            step_outs = 0
            for i in range(m):
                for j in range(n):
                    # Check if the point is reachable
                    curr_mult = curr_tbl[i][j]
                    curr_outs = 0
                    if 0 == curr_mult:
                        continue
                    # Check if we can move
                    if 0 == i:
                        curr_outs += curr_mult
                    else:
                        next_tbl[i - 1][j] += curr_mult
                    if i + 1 == m:
                        curr_outs += curr_mult
                    else:
                        next_tbl[i + 1][j] += curr_mult
                    if 0 == j:
                        curr_outs += curr_mult
                    else:
                        next_tbl[i][j - 1] += curr_mult
                    if j + 1 == n:
                        curr_outs += curr_mult
                    else:
                        next_tbl[i][j + 1] += curr_mult

                    step_outs = (step_outs + curr_outs) % MOD

            num_outs = (num_outs + step_outs) % MOD
            # print('>> step', step, '#outs', step_outs)
            # for r in range(m):
            #     print(' '.join(map(str, curr_tbl[r])))
            # print('----')

            curr_tbl = next_tbl
            next_tbl = gen_new_tbl()

        return int(num_outs)


import numpy as np


class Solution_1(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int

        """
        paths = np.zeros((m, n), dtype=np.int64)
        paths[i][j] = 1
        out = 0
        mod = 10 ** 9 + 7
        for _ in range(N):
            prev = paths % mod
            paths = prev - prev
            paths[1:] += prev[:-1]
            paths[:-1] += prev[1:]
            paths[:, 1:] += prev[:, :-1]
            paths[:, :-1] += prev[:, 1:]
            out += 4 * prev.sum() - paths.sum()
        return int(out % mod)
m = 1
n = 3
N = 3
i = 0
j = 1
print(Solution().findPaths(m, n, N, i, j))