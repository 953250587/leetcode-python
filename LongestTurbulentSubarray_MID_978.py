# -*- coding: UTF-8 -*-
"""
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:
For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
Return the length of a maximum size turbulent subarray of A.

Example 1:
Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:
Input: [4,8,12,16]
Output: 2
Example 3:
Input: [100]
Output: 1

Note:
1 <= A.length <= 40000
0 <= A[i] <= 10^9
"""


class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        936 ms
        15.2 MB
        """
        if len(A) <= 0:
            return 0
        max_len = 1
        start = A[0]
        # 从奇数情况考虑
        flag = 'odd'
        cur_len = 1
        for i in range(1, len(A)):
            # 如果当前是偶数
            if i % 2 == 0:
                # 处于奇数模式下,奇数<偶数,当前长度+1
                if flag == 'odd' and start > A[i]:
                    cur_len += 1
                elif flag == 'odd':
                    # 如果在奇数模式下,奇数>偶数,说明可以转化为偶数模式
                    if start < A[i]:
                        cur_len = 2
                    # 否则说明当前模式不确定
                    else:
                        cur_len = 1
                    flag = 'even'
                # 偶数模式下类似
                elif flag == 'even' and start < A[i]:
                    cur_len += 1
                else:
                    if start > A[i]:
                        cur_len = 2
                    else:
                        cur_len = 1
                    flag = 'odd'
            else:
                if flag == 'odd' and start < A[i]:
                    cur_len += 1
                elif flag == 'odd':
                    if start > A[i]:
                        cur_len = 2
                    else:
                        cur_len = 1
                    flag = 'even'
                elif flag == 'even' and start > A[i]:
                    cur_len += 1
                else:
                    if start < A[i]:
                        cur_len = 2
                    else:
                        cur_len = 1
                    flag = 'odd'
            start = A[i]
            max_len = max(max_len, cur_len)
        return max_len

    def maxTurbulenceSize_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        984 ms
        15.6 MB
        """
        '''
        let L[i] be the maximum size of turbulent array ending at A[i], then
        if A[i] < A[i - 1] > A[i - 2], then L[i] = L[i - 1] + 1
        if A[i] > A[i - 1] < A[i - 2], then L[i] = L[i - 1] + 1
        if A[i] == A[i - 1] L[i] = 1
        else L[i] = 2
        '''
        n = len(A)
        ans = a = 0
        if n >= 1:
            ans = a = 1
        if n >= 2:
            if A[0] == A[1]:
                ans = a = 1
            else:
                ans = a = 2
        for i in range(2, n):
            if (A[i] < A[i - 1] and A[i - 1] > A[i - 2]) or (A[i] > A[i - 1] and A[i - 1] < A[i - 2]):
                b = 1 + a
            elif A[i] == A[i - 1]:
                b = 1
            else:
                b = 2
            a = b
            # print(a)
            ans = max(ans, a)
        return ans

if __name__ == '__main__':
    print(Solution().maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(Solution().maxTurbulenceSize([4,8,12,16]))
    print(Solution().maxTurbulenceSize([100]))



