"""
Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A.

As the answer may be very large, return the answer modulo 10^9 + 7.



Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.


Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000
"""


class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        140 ms
        """
        A = sorted(A)
        l = len(A)
        list_2 = [1]
        k = 10 ** 9 + 7
        ans = 0
        for i in range(1, l + 1):
            list_2.append(list_2[-1] * 2 % k)
        for i in range(1, l):
            ans += ((A[i] - A[i - 1]) * (list_2[-1] - list_2[i] - list_2[l - i] + 1) % k)
            ans %= k
        return ans
print(Solution().sumSubseqWidths([2, 1, 3]))






