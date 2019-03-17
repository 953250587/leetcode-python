"""
 Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input:

0 0 0
0 1 0
0 0 0

Output:

0 0 0
0 1 0
0 0 0

Example 2:
Input:

0 0 0
0 1 0
1 1 1

Output:

0 0 0
0 1 0
1 2 1

Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.


"""
import numpy as np
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        693ms
        """
        l = len(matrix)
        r = len(matrix[0])
        self.matrix = matrix
        mat = [[-1] * r for i in range(l)]

        quene = []
        for i in range(l):
            for j in range(r):
                if self.matrix[i][j] == 0:
                    mat[i][j] = 0
                    if i - 1 >= 0 and self.matrix[i - 1][j] == 1 and mat[i - 1][j] == -1:
                        mat[i - 1][j] = -2
                        quene.append((i - 1, j))
                    if j - 1 >= 0 and self.matrix[i][j - 1] == 1 and mat[i][j - 1] == -1:
                        mat[i][j - 1] = -2
                        quene.append((i, j - 1))
                    if j + 1 < r and self.matrix[i][j + 1] == 1 and mat[i][j + 1] == -1:
                        mat[i][j + 1] = -2
                        quene.append((i, j + 1))
                    if i + 1 < l and self.matrix[i + 1][j] == 1 and mat[i + 1][j] == -1:
                        mat[i + 1][j] = -2
                        quene.append((i + 1, j))
        print(quene)
        count = 0
        while quene:
            new_quene = []
            count += 1
            for ite in quene:
                i, j = ite[0], ite[1]
                mat[i][j] = count
                print('1', np.array(mat))
                if i - 1 >= 0 and mat[i - 1][j] == -1:
                    mat[i - 1][j] = -2
                    new_quene.append((i - 1, j))
                if j - 1 >= 0 and mat[i][j - 1] == -1:
                    mat[i][j - 1] = -2
                    new_quene.append((i, j - 1))
                if j + 1 < r and mat[i][j + 1] == -1:
                    mat[i][j + 1] = -2
                    new_quene.append((i, j + 1))
                if i + 1 < l and mat[i + 1][j] == -1:
                    mat[i + 1][j] = -2
                    new_quene.append((i + 1, j))
            print(new_quene)
            quene = new_quene
        return mat

    def updateMatrix_1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        602ms
        """
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])

        def whether_levelup(y, x, level):
            if y - 1 >= 0 and matrix[y - 1][x] < level: return False
            if y + 1 < m and matrix[y + 1][x] < level: return False
            if x - 1 >= 0 and matrix[y][x - 1] < level: return False
            if x + 1 < n and matrix[y][x + 1] < level: return False
            return True

        dq = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1: dq.append((i, j))
        level = 1
        while dq:
            level_up = []
            for r, c in dq:
                if whether_levelup(r, c, level):
                    level_up.append((r, c))
            for r, c in level_up:
                matrix[r][c] = level + 1
            level += 1
            dq = level_up
        return matrix


matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
print(Solution().updateMatrix(matrix))

matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
print(Solution().updateMatrix(matrix))