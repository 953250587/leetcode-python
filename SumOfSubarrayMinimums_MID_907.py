"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.


Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000
"""
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        208 ms   # 记录左右两边能扩展的最大位置，第一次向前记录左边，stack跳出记录右边
        """
        stack = []
        ans = 0
        for i, a in enumerate(A):
            ans += a
            left = 0
            right = 0
            while stack and stack[-1][0] >= a:
                temp = stack.pop()
                left += temp[1] + 1
                ans += (temp[1] + right + temp[1] * right) * temp[0]
                ans %= 10 ** 9 + 7
                right += temp[1] + 1
            stack.append([a, left])
            print('gg', stack, ans)
        right = 0
        while stack:
            temp = stack.pop()
            ans += (temp[1] + right + temp[1] * right) * temp[0]
            ans %= 10 ** 9 + 7
            right += temp[1] + 1
            print('ss', stack, ans)
        return ans

    def sumSubarrayMins_1(self, A):
        """
        444ms
        :param A:
        :return:
        """
        n, mod = len(A), 10 ** 9 + 7
        left, right, s1, s2 = [0] * n, [0] * n, [], []
        for i in range(n):
            count = 1
            while s1 and s1[-1][0] > A[i]: count += s1.pop()[1]
            left[i] = count
            s1.append([A[i], count])
        for i in range(n)[::-1]:
            count = 1
            while s2 and s2[-1][0] >= A[i]: count += s2.pop()[1]
            right[i] = count
            s2.append([A[i], count])
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod
print(Solution().sumSubarrayMins([3,1,2,4]))
print(Solution().sumSubarrayMins([85,93,93,90]))
