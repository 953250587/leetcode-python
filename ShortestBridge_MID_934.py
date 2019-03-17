"""
In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)



Example 1:

Input: [[0,1],[1,0]]
Output: 1
Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Note:

1 <= A.length = A[0].length <= 100
A[i][j] == 0 or A[i][j] == 1
"""


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        192 ms
        """
        row = len(A)
        column = len(A[0])
        # 先找出每个岛屿的范围，用dfs搜索
        def dfs(start_point_x, start_point_y, island):
            if A[start_point_x][start_point_y] != 1:
                return island
            A[start_point_x][start_point_y] = -1
            island.add((start_point_x, start_point_y))
            for dic in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                if 0 <= start_point_x + dic[0] < row and 0 <= start_point_y + dic[1] < column:
                    island = dfs(start_point_x + dic[0], start_point_y + dic[1], island)
            return island
        # 找出其中一个岛的情况
        island = set()
        def find_island(island):
            for i in range(row):
                for j in range(column):
                    if A[i][j] == 1:
                        island = dfs(i, j, island)
                        return island
        island = find_island(island)
        # 用bfs搜索最近路线
        def bfs(island):
            count = 0
            while island:
                # 存储下一次可以移动的点
                next_island = set()
                for start_point_x, start_point_y in island:
                    for dic in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        if 0 <= start_point_x + dic[0] < row and 0 <= start_point_y + dic[1] < column:
                            if A[start_point_x + dic[0]][start_point_y + dic[1]] == 0:
                                next_island.add((start_point_x + dic[0], start_point_y + dic[1]))
                                # 走过的点就标记掉
                                A[start_point_x + dic[0]][start_point_y + dic[1]] = -1
                            elif A[start_point_x + dic[0]][start_point_y + dic[1]] == 1:
                                return count
                island = next_island
                count += 1
            return 1

        return bfs(island)



print(Solution().shortestBridge([[0,1],[1,0]]))
print(Solution().shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(Solution().shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))

from collections import deque


class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        76ms
        """
        # 只找到一个点，就开始bfs扩散
        N = len(A)
        M = len(A[0])

        startI = -1
        startJ = -1
        for i in range(N):
            if startI >= 0:
                break
            for j in range(M):
                if A[i][j] == 1:
                    startI = i
                    startJ = j
                    break

        boundaryWater = deque()
        A[startI][startJ] = 2
        queue = deque()
        queue.append((startI, startJ))

        while len(queue) > 0:
            currentI, currentJ = queue.popleft()
            for deltaI, deltaJ in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nextI = currentI + deltaI
                nextJ = currentJ + deltaJ
                if nextI < 0 or nextI == N or nextJ < 0 or nextJ == M:
                    continue
                if A[nextI][nextJ] == 2:
                    continue
                elif A[nextI][nextJ] == 0:
                    A[nextI][nextJ] = 2
                    boundaryWater.append((nextI, nextJ, 1))
                else:
                    A[nextI][nextJ] = 2
                    queue.append((nextI, nextJ))

        while len(boundaryWater) > 0:
            currentI, currentJ, distance = boundaryWater.popleft()
            for deltaI, deltaJ in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                nextI = currentI + deltaI
                nextJ = currentJ + deltaJ
                if nextI < 0 or nextI == N or nextJ < 0 or nextJ == M:
                    continue
                if A[nextI][nextJ] == 2:
                    continue
                elif A[nextI][nextJ] == 1:
                    return distance
                else:
                    A[nextI][nextJ] = 2
                    boundaryWater.append((nextI, nextJ, distance + 1))