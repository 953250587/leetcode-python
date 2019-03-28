# -*- coding: UTF-8 -*-
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        388 ms
        13.9 MB
        """
        """
        O(n)方案,需要两次遍历
        """
        ans = []
        # 先找到正数与负数的分割位置
        # 默认分割位置为最末尾
        split = len(A)
        for i, a in enumerate(A):
            if a > 0:
                split = i
                break
        # 不大于0的部分
        left_max = split - 1
        # 大于0的部分
        right_min = split
        # 从中间往两边扩散
        while left_max >= 0 and right_min < len(A):
            # 谁小取谁
            if A[left_max] ** 2 < A[right_min] ** 2:
                ans.append(A[left_max] ** 2)
                left_max -= 1
            else:
                ans.append(A[right_min] ** 2)
                right_min += 1
        # 如果左边还有
        while left_max >= 0:
            ans.append(A[left_max] ** 2)
            left_max -= 1
        # 如果右边还有
        while right_min < len(A):
            ans.append(A[right_min] ** 2)
            right_min += 1

        return ans

if __name__ == '__main__':
    print(Solution().sortedSquares([-4,-1,0,3,10]))
    print(Solution().sortedSquares([-7,-3,2,3,11]))
    print(Solution().sortedSquares([1, 2, 3, 11]))
    print(Solution().sortedSquares([-11, -3, -2, -1]))

