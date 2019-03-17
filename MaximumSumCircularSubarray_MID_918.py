"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""


class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        216 ms
        """
        # 判断是否是在正中间的某一段
        total = 0
        max_value = -float('inf')
        for a in A:
            if total < 0:
                total = 0
            total += a
            max_value = max(max_value, total)
        # 判断是否在头尾相连的部分
        total = 0
        min_value = float('inf')
        for a in A:
            if total > 0:
                total = 0
            total += a
            min_value = min(min_value, total)
        temp = sum(A) - min_value
        # 排除整个都被删除的情况，然后比较两种中的最大值最为输出
        return max(max_value, temp if temp != 0 else max_value)

    def maxSubarraySumCircular_1(self, A):
        """
        :type A: List[int]
        :rtype: int
        116ms
        """
        m = 0
        maxsum = -30000
        minussum = -30000
        for i in A:
            if m < 0:
                m = i
            else:
                m += i
            if m > maxsum:
                maxsum = m
        m = 0
        allinclude = True
        for i in A:
            i = -i
            if m < 0:
                m = i
                allinclude = False
            else:
                m += i
            if m > minussum:
                minussum = m
        if not allinclude:
            return max(maxsum, sum(A) + minussum)
        else:
            return maxsum



print(Solution().maxSubarraySumCircular([1,-2,3,-2]))  # 3
print(Solution().maxSubarraySumCircular([5,-3,5]))  # 10
print(Solution().maxSubarraySumCircular([3,-1,2,-1]))  # 4
print(Solution().maxSubarraySumCircular([3,-2,2,-3]))  # 3
print(Solution().maxSubarraySumCircular([-2,-3,-1]))  # -1
print(Solution().maxSubarraySumCircular([3,-2,2,-3,3]))  # 6
print(Solution().maxSubarraySumCircular([3,-1,-3,-1,4]))  # 7
print(Solution().maxSubarraySumCircular([3,1,3,2,6]))  # 15
print(Solution().maxSubarraySumCircular([5,5,0,-5,3,-3,2]))  # 12



