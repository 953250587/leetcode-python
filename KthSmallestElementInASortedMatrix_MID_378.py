"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""
import heapq
import bisect
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        302ms
        """
        if len(matrix)<=0:
            return 0

        m=len(matrix)
        mat = [(matrix[0][0],(0,0))]
        self.sets=set()
        self.sets.add((0,0))

        heapq.heapify(mat)
        result = 0
        while k > 0 and mat:
            elem = heapq.heappop(mat)
            # print(elem)
            result=elem[0]
            if elem[1][0] + 1 < m and (elem[1][0]+1, elem[1][1]) not in self.sets:
                heapq.heappush(mat, (matrix[elem[1][0] + 1][elem[1][1]], (elem[1][0]+1, elem[1][1])))
                self.sets.add((elem[1][0]+1, elem[1][1]))
            if elem[1][1] + 1 < m and (elem[1][0], elem[1][1]+1) not in self.sets:
                heapq.heappush(mat, (matrix[elem[1][0]][elem[1][1]+1], (elem[1][0], elem[1][1]+1)))
                self.sets.add((elem[1][0], elem[1][1]+1))
            k -= 1
        # print(self.sets)
        return result

    def kthSmallest_1(self, matrix, k):
        """
        :param matrix:
        :param k:
        :return:
         59ms
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = (lo + hi) // 2
            # bisect_left 和 bisect_right 函数，该函数用入处理将会插入重复数值的情况，返回将会插入的位置：
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def kthSmallest_3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        158ms
        """
        """
        Build a min-heap with the first row of the matrix and store row, col.
        Repeat the following k times:
            Get the top of heap and replace it with element at row+1, col
        The last element removed from top of heap is the answer.
        It works because at ith iteration we just add the next highest number from the corresponding column,
        but still the top of heap has ith largest number from the numbers seen so far.
        """
        if len(matrix) == 0:
            return -1

        row_size, col_size = len(matrix), len(matrix[0])
        heap = []
        for j in range(col_size):
            heapq.heappush(heap, (matrix[0][j], 0, j))

        num, r, c = None, None, None
        for i in range(k):
            num, r, c = heapq.heappop(heap)
            if r + 1 < row_size:
                heapq.heappush(heap, (matrix[r + 1][c], r + 1, c))

        return num
matrix = [[1,3,5],[6,7,12],[11,14,14]]
k = 6
print(Solution().kthSmallest(matrix,k))