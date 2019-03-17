"""
 Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:
          S MODEL
Note:

    The total number of elements of the given matrix will not exceed 10,000.

"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        839ms
        """
        count = 0
        M = len(matrix)
        if M <= 0:
            return []
        N = len(matrix[0])
        result=[]
        for i in range(M + N - 1):
            if count % 2 == 1:
                a = max(i - N + 1, 0)
                for j in range(a, M):
                    if i - j >= N or i - j < 0:
                        break
                    result.append(matrix[j][i - j])
            else:
                for j in range(min(M - 1, i), -1, -1):
                    if i - j >= N or i - j < 0:
                        break
                    result.append(matrix[j][i - j])
            count += 1
        return result

    def findDiagonalOrder_1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        result = []
        updown = 1
        i = 0
        j = 0

        while i < m and j < n:
            result.append(matrix[i][j])

            if updown == 1:
                i -= 1
                j += 1

            else:
                i += 1
                j -= 1

            # if we get right up coner
            if i < 0 and j >= n:
                i = 1
                j = n - 1
                updown *= -1

            # if we get left down coner
            elif j < 0 and i >= m:
                i = m - 1
                j = 1
                updown *= -1

            # if we get the top bound
            elif i < 0:
                i = 0
                updown *= -1

            elif j < 0:
                j = 0
                updown *= -1

            elif i >= m:
                i = m - 1
                j += 2
                updown *= -1

            elif j >= n:
                j = n - 1
                i += 2
                updown *= -1

        return result

    def findDiagonalOrder_2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        199ms
        """
        if not matrix: return []
        nRow = len(matrix)
        nCol = len(matrix[0])
        if nCol == 0:
            return []
        elif nRow == 1:
            return matrix[0]
        elif nCol == 1:
            return [r[0] for r in matrix]

        i, j = 0, 0
        result = [matrix[i][j]]
        while len(result) < nRow * nCol:
            if i == 0 and j < nCol - 1:
                j += 1
                while i < nRow - 1 and j > 0:
                    result.append(matrix[i][j])
                    if i == nRow and j == nCol:
                        return result
                    i += 1
                    j -= 1
                result.append(matrix[i][j])
                if i >= nRow - 1 and j >= nCol - 1:
                    return result

            if i >= 0 and j >= nCol - 1:
                i += 1
                while i < nRow - 1 and j > 0:
                    result.append(matrix[i][j])
                    i += 1
                    j -= 1
                result.append(matrix[i][j])
                if i >= nRow - 1 and j >= nCol - 1:
                    return result

            if j == 0 and i < nRow - 1:
                i += 1
                while i > 0 and j < nCol - 1:
                    result.append(matrix[i][j])
                    if i == nRow and j == nCol:
                        return result
                    i -= 1
                    j += 1
                result.append(matrix[i][j])
                if i >= nRow - 1 and j >= nCol - 1:
                    return result

            if j >= 0 and i >= nRow - 1:
                j += 1
                while i > 0 and j < nCol - 1:
                    result.append(matrix[i][j])
                    if i == nRow and j == nCol:
                        return result
                    i -= 1
                    j += 1
                result.append(matrix[i][j])
                if i >= nRow - 1 and j >= nCol - 1:
                    return result
        return result
matrix=[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(Solution().findDiagonalOrder(matrix))

matrix=[
 [ 1, 2, 6, 7],
 [ 3, 5, 8, 11],
 [ 4, 9, 10, 12]
]
print(Solution().findDiagonalOrder(matrix))

matrix=[[1, 2, 3]]
print(Solution().findDiagonalOrder(matrix))