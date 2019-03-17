"""
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K) 	-3 	3
-5 	-10 	1
10 	30 	-5 (P)

Notes:

    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

"""
import numpy as np
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        55ms
        """
        m = len(dungeon)
        if m <= 0:
            return 1
        n = len(dungeon[0])
        dp = [[0] * n for _ in range(m)]
        dp[-1][-1] = -min(0, dungeon[-1][-1]) + 1
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(dp[i + 1][-1] - dungeon[i][-1], 1)
        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(dp[-1][j + 1] - dungeon[-1][j], 1)
        print(np.array(dp))
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]), 1)
        print(np.array(dp))
        return dp[0][0]

    def calculateMinimumHP1(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon[0])
        need = [2 ** 31] * (n - 1) + [1]
        for row in dungeon[::-1]:
            for j in range(n)[::-1]:
                need[j] = max(min(need[j:j + 2]) - row[j], 1)
        return need[0]

    def calculateMinimumHP_1(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        39ms
        """
        import sys
        M = len(dungeon)
        N = len(dungeon[0])
        hp = [[sys.maxsize] * (N + 1) for i in xrange(M + 1)]
        hp[M][N - 1] = 1
        hp[M - 1][N] = 1
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                need = min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j]
                if need <= 0:
                    hp[i][j] = 1
                else:
                    hp[i][j] = need
        return hp[0][0]


dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
print(Solution().calculateMinimumHP(dungeon))

dungeon = [[2],[1]]
print(Solution().calculateMinimumHP(dungeon))
