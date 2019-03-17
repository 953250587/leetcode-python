"""
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)



Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]


Note:

1 <= N <= 1000
"""


class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        32 ms
        """
        # 分成奇数偶数的情况！！！！！分治！！！！牛逼！！！
        res = [1]
        while len(res) < N:
            res = [i * 2 - 1 for i in res] + [i * 2 for i in res]
        return [i for i in res if i <= N]


print(Solution().beautifulArray(4))
print(Solution().beautifulArray(5))
print(Solution().beautifulArray(6))