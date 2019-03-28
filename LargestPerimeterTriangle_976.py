# -*- coding: UTF-8 -*-
"""
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.
If it is impossible to form any triangle of non-zero area, return 0.


Example 1:
Input: [2,1,2]
Output: 5
Example 2:
Input: [1,2,1]
Output: 0
Example 3:
Input: [3,2,3,4]
Output: 10
Example 4:
Input: [3,6,2,3]
Output: 8

Note:
3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""


class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        400 ms
        13 MB
        """
        """
        O(nlgn),要找三角形最大周长,肯定首选最长的两条边,之后只要剩下最长的边比前两条边的差小就可以围成三角形
        如果不行,则说明最长边太长了,就算替换第二长的边,两边只差只会增大,更不可能满足条件
        所以需要替换最长边,以此类推知道不能继续或者成功构建三角形
        """
        A = sorted(A)
        for i in range(2, len(A))[::-1]:
            if A[i] - A[i - 1] < A[i - 2]:
                return sum(A[i - 2: i + 1])
        return 0


if __name__ == '__main__':
    print(Solution().largestPerimeter([1,2,1]))
    print(Solution().largestPerimeter([3,2,3,4]))
    print(Solution().largestPerimeter([3,6,2,3]))
