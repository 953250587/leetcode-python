"""
We are given an array A of positive integers, and two positive integers L and R (L <= R).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least L and at most R.

Example :
Input:
A = [2, 1, 4, 3]
L = 2
R = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].

Note:

    L, R  and A[i] will be an integer in the range [0, 10^9].
    The length of A will be in the range of [1, 50000].


"""


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        123ms
        """
        # 找出所有比R大的元素的位置
        bigger_R = []
        for i, a in enumerate(A):
            if a > R:
                bigger_R.append(i)
        start = 0
        sub_range = []
        # 按比R大的元素把原来区间划分为更小的区间
        for high in bigger_R:
            if high > start:
                sub_range.append((start, high))
            start = high + 1
        # 考虑最后一段需不需要加入
        if start < len(A):
            sub_range.append((start, len(A)))
        print(sub_range)
        # 对每个区间的值相加
        ans = 0
        for one_range in sub_range:
            before_one = 0
            for i in range(one_range[1] - 1, one_range[0] - 1, -1):
                if A[i] >= L:
                    before_one = one_range[1] - i
                ans += before_one
        return ans

    def numSubarrayBoundedMax_1(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        111ms
        """
        res, dp = 0, 0
        prev = -1
        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res
print(Solution().numSubarrayBoundedMax(A = [2, 1, 4, 3],L = 2,R = 3))

