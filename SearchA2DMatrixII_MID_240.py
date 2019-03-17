"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        168ms
        """
        self.row=len(matrix)
        if self.row<=0:
            return False
        self.column = len(matrix[0])
        if self.column<=0:
            return False
        def search_start(target,i,j):
            if matrix[i][j]==target:
                return i,j
            if (matrix[i][j]<target and i+1<self.row and matrix[i+1][j]>target) or (i+1>=self.row):
                return i,j
            else:
                return search_start(target,i+1,j)
        def search(target,i,j):
            print((i,j))
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]<target:
                if j+1<self.column:
                    return search(target,i,j+1)
                else:
                    return False
            else:
                if i-1>=0:
                    return search(target,i-1,j)
                else:
                    return False
        i,j=search_start(target,0,0)
        return search(target,i,j)
        # print(search_start(target,0,0))

    def searchMatrix_1(self, matrix, target):
        # 96ms
        self.row = len(matrix)
        if self.row <= 0:
            return False
        self.column = len(matrix[0])
        if self.column <= 0:
            return False
        m, n, r = len(matrix), len(matrix[0]), 0
        c = n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False

    def searchMatrix_2(self, matrix, target):
        # 92ms
        self.row = len(matrix)
        if self.row <= 0:
            return False
        self.column = len(matrix[0])
        if self.column <= 0:
            return False
        if matrix:
            row, col, width = len(matrix) - 1, 0, len(matrix[0])
            while row >= 0 and col < width:
                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] > target:
                    row -= 1
                else:
                    col += 1
            return False
matrix=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(Solution().searchMatrix(matrix,20))
