"""
 On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:

Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.

Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""
import numpy as np
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        385ms
        """
        dp = [[0] * N for i in range(N)]
        self.N = N

        def postion(r, c):
            pos = set()
            lists = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                     (2, 1), (1, 2), (-1, 2), (-2, 1)]
            for i in lists:
                x = r + i[0]
                y = c + i[1]
                if (x >= 0 and x < self.N) and (y >= 0 and y < self.N):
                    pos.add((x, y))
            return pos

        sets = {(r, c)}
        dp[r][c] = 1

        for k in range(1, K + 1):
            dp_2 = [[0] * N for i in range(N)]
            set_2 = set()
            for i in sets:
                pos = postion(i[0], i[1])
                for p in pos:
                    dp_2[p[0]][p[1]] += 0.125  * dp[i[0]][i[1]]
                    set_2.add(p)
            dp = dp_2
            sets = set_2
            # print(np.array(dp))
        s = 0
        for i in dp:
            s += sum(i)
        return s

    def knightProbability_1(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        192ms
        """
        moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
        dests = [[[] for _ in range(N)] for _ in range(N)]
        for x in range(N):
            for y in range(N):
                for move in moves:
                    nx, ny = x + move[0], y + move[1]
                    if nx >= 0 and nx < N and ny >= 0 and ny < N:
                        dests[x][y].append((nx, ny))

        m0 = [[1] * N for _ in range(N)]
        for i in range(K):
            m1 = [[0] * N for _ in range(N)]
            for x in range(N):
                for y in range(N):
                    for dest in dests[x][y]:
                        m1[x][y] += m0[dest[0]][dest[1]]
            m0 = m1

        return 1.0 * m0[r][c] / (8 ** K)

    def knightProbability_2(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        152ms
        """
        pdf = [[0 for _ in range(N)] for _ in range(N)]
        pdf[r][c] = 1
        for _ in range(K):
            #            print pdf
            newPDF = [[0 for _ in range(N)] for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    if pdf[i][j] > 0:
                        p = pdf[i][j] / 8.0
                        if i > 1:
                            if j > 0:
                                newPDF[i - 2][j - 1] += p
                            if j < N - 1:
                                newPDF[i - 2][j + 1] += p
                        if i > 0:
                            if j > 1:
                                newPDF[i - 1][j - 2] += p
                            if j < N - 2:
                                newPDF[i - 1][j + 2] += p
                        if i < N - 2:
                            if j > 0:
                                newPDF[i + 2][j - 1] += p
                            if j < N - 1:
                                newPDF[i + 2][j + 1] += p
                        if i < N - 1:
                            if j > 1:
                                newPDF[i + 1][j - 2] += p
                            if j < N - 2:
                                newPDF[i + 1][j + 2] += p
            pdf = newPDF

            #        print pdf

        return sum([i for j in pdf for i in j])


print(Solution().knightProbability(25, 100, 0, 0))


