"""
Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.



Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.



Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
"""


class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        136 ms
        """
        if len(A) <= 0:
            return 0
        l = len(A[0])
        # 记忆数组
        memory = {}
        def dfs(row, column):
            if (row, column) in memory:
                return memory[(row, column)]
            if row == len(A) - 1:
                return A[row][column]
            min_val = float('inf')
            # 在可以走的范围内搜索
            for next_column in range(max(0, column - 1), min(l - 1, column + 1) + 1):
                min_val = min(min_val, dfs(row + 1, next_column) + A[row][column])
            memory[(row, column)] = min_val
            return min_val

        temp = min([dfs(0, i) for i in range(l)])
        # print(memory)
        return temp

    def minFallingPathSum_1(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        40ms
        """
        l = len(A)
        sums1 = A[0]
        for i in range(1, l):
            sums2 = [min(sums1[0], sums1[1]) + A[i][0]]
            for j in range(1, l - 1):
                sums2.append(min(sums1[j - 1], sums1[j], sums1[j + 1]) + A[i][j])
            sums2.append(min(sums1[l - 2], sums1[l - 1]) + A[i][l - 1])
            sums1 = sums2
        return min(sums1)


print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().minFallingPathSum([[17,82],[1,-44]]))
