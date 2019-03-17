"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

"""
import numpy as np
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        4592ms
        """
        m, n = len(A) + 1, len(B) + 1
        dp = [0] * (n)
        ret = 0
        for i in range(1, m):
            pre = 0
            for j in range(1, n):
                tmp = dp[j]
                if A[i - 1] == B[j - 1]:
                    dp[j] = 1 + pre
                    ret = max(ret, dp[j])
                else:
                    dp[j] = 0
                pre = tmp
        return ret

    def findLength_1(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        3092ms
        """
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)

    def findLength_2(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        142ms
        """
        if len(A) > len(B): return self.findLength_2(B, A)

        def check(length):
            lookup = set(A[i:i + length] \
                         for i in range(len(A) - length + 1))
            return any(B[j:j + length] in lookup \
                       for j in range(len(B) - length + 1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))
        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = left + (right - left) / 2
            if not check(mid):  # find the min idx such that check(idx) == false
                right = mid
            else:
                left = mid + 1
        return left - 1
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(Solution().findLength(A, B))

A = [0,0,0,0,1]
B = [1,0,0,0,0]
print(Solution().findLength(A, B))

A = [0,0,0,0,0,0,1,0,0,0]
B = [0,0,0,0,0,0,0,1,0,0]
print(Solution().findLength(A, B))

A = [0,1,1,1,1]
B = [1,0,1,0,1]