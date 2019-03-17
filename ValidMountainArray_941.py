"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]


Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true


Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
"""


class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        36 ms
        """
        l = len(A)
        # 长度不够
        if l < 3:
            return False
        flag = l - 1
        for i in range(1, l):
            if A[i - 1] < A[i]:
                continue
            # 如果相等肯定不行
            elif A[i - 1] == A[i]:
                return False
            # 顶峰的位置
            else:
                flag = i - 1
                break
        # 顶峰在开头或者结尾都不行
        if flag == l - 1 or flag == 0:
            return False
        # 确保之后都是递减
        return all([A[i] > A[i + 1] for i in range(flag, l - 1)])

    def validMountainArray_1(self, A):
        """
        :type A: List[int]
        :rtype: bool
        36ms
        """
        if len(A) < 3:
            return False
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                break
        else:
            return False
        if i == 1:
            return False
        for j in range(i - 1, len(A) - 1):
            if A[j] <= A[j + 1]:
                return False
        return True


print(Solution().validMountainArray([2,1]))
print(Solution().validMountainArray([3,5,5]))
print(Solution().validMountainArray([0,3,2,1]))
print(Solution().validMountainArray([3,2,1]))
print(Solution().validMountainArray([3,3,2,1]))
print(Solution().validMountainArray([0,1,2,1,0]))
print(Solution().validMountainArray([0,1,2,3]))