"""
 Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6.
"""
import numpy as np


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        82ms
        """
        if not heights:
            return 0
        stack = []
        max_area = heights[0]
        stack.append([0, heights[0]])
        for i, height in enumerate(heights[1:]):
            a = i + 1
            # print('i', a, height)
            if height > stack[-1][-1]:
                stack.append([a, height])
            else:
                while stack and stack[-1][-1] >= height:
                    b = stack.pop()
                    # print('b', b)
                    max_area = max(max_area, b[-1] * (a - b[0]))
                b[-1] = height
                max_area = max(max_area, (a - b[0] + 1) * height)
                stack.append(b)
            # print(stack)
            # print(max_area)
        l = len(heights)
        for i in stack:
            max_area = max(max_area, (l - i[0]) * i[1])
        return max_area
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        179ms
        """
        max_1 = 0
        m = len(matrix)
        if m <=0 :
            return 0
        n = len(matrix[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[j] = 0
                else:
                    dp[j] += 1
            max_1 = max(max_1, self.largestRectangleArea(dp))
        return max_1

    def maximalRectangle_1(self, matrix):
        """
        128ms
        :param matrix:
        :return:
        """
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))