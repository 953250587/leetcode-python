"""
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.



Example 1:

Input: A = [1], K = 0
Output: 0
Explanation: B = [1]
Example 2:

Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]
Example 3:

Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]


Note:

1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""


class Solution(object):
    def smallestRangeII(self, A, K):
        """
        理解错误，我选择的是0-K范围内的，使得整个最小，而题目是给定了K
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) <= 1:
            return 0
        A = sorted(A)
        def min_len(low_1, high_1, low_2, high_2, K):
            # 找出两端最低点之间的差值
            assert low_2 - low_1 >= 0
            temp = low_2 - low_1
            # 判读能不能再2*K的范围内
            if temp <= 2 * K:
                # 如果能被2整除，则考虑把最低点放到一起，然后比较最高点，得到结果
                if temp % 2 == 0:
                    return max(high_2 - low_2, high_1 - low_1)
                # 否则则要考虑是选择上移一位还是下移一位，然后比较两种情况中的比较小的那个
                else:
                    print('temp', temp)
                    return min(max(high_1, high_2 - temp - 1) - min(low_1, low_2 - temp - 1),
                               max(high_1, high_2 - temp + 1) - min(low_1, low_2 - temp + 1))
            # 否则则考虑两端最大高度之间的最大值和low_1之间的距离
            else:
                return max(high_1, high_2 - 2 * K) - low_1
        min_1 = float('inf')
        for i in range(len(A) - 1):
            min_1 = min(min_1, min_len(A[0], A[i], A[i + 1], A[-1], K))
            print(min_1, i, A[i])
        return min_1


    def smallestRangeII_1(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        72 ms
        """
        if len(A) <= 1:
            return 0
        A = sorted(A)

        def min_len(low_1, high_1, low_2, high_2, K):
            # 找出两端最低点之间的差值
            assert low_2 - low_1 >= 0
            return max(high_1, high_2 - 2 * K) - min(low_1, low_2 - 2 * K)
        # 保证原来的值为起始值
        min_1 = A[-1] - A[0]
        for i in range(len(A) - 1):
            min_1 = min(min_1, min_len(A[0], A[i], A[i + 1], A[-1], K))
            # print(min_1, i, A[i])
        return min_1

    def smallestRangeII_2(self, A, K):
        """
        68ms
        :param A:
        :param K:
        :return:
        """
        ma, mi = max(A), min(A)
        if ma - mi >= 4 * K: return ma - mi - 2 * K
        if ma - mi <= K: return ma - mi
        inter = sorted([i for i in A if ma - 2 * K < i < mi + 2 * K] + [ma - 2 * K, mi + 2 * K])
        return min(a + 2 * K - b for a, b in zip(inter, inter[1:]))

# print(Solution().smallestRangeII_1(A=[1], K=0))
# print(Solution().smallestRangeII_1(A=[0, 10], K=2))
# print(Solution().smallestRangeII_1(A=[1, 3, 6], K=3))
print(Solution().smallestRangeII_1([7, 8, 8], 5))