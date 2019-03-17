"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.



Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true


Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000

"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        132ms
        """
        def cmp(i, j):
            if i > j:
                return 1
            elif i < j:
                return -1
            else:
                return 0
        print({cmp(i, j) for i, j in zip(A, A[1:])})
        print({cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1})
        return not {cmp(i, j) for i, j in zip(A, A[1:])} >= {1, -1}

print({1, 2} >= {2, 1})
# print(Solution().isMonotonic([1,2,2,3]))
# print(Solution().isMonotonic([6,5,4,4]))
# print(Solution().isMonotonic([1,3,2]))
# print(Solution().isMonotonic([1,2,4,5]))
# print(Solution().isMonotonic([1,1,1]))
# print(Solution().isMonotonic([1,2,3,2,1]))
