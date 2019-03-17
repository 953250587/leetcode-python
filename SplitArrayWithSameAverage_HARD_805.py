"""
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input:
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.

Note:

    The length of A will be in the range [1, 30].
    A[i] will be in the range of [0, 10000].

"""


class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        2272 ms!!!!!!!!
        """
        s = sum(A)
        l = len(A)
        if l == 1:
            return False
        avg = s / l
        print(avg)
        dp = [[set() for _ in range(l + 1)] for _ in range(l + 1)]
        for i in range(1, l + 1):

            dp[i][0].add(0)
        dp[1][1].add(A[0])
        if A[0] == avg:
            return True
        for i in range(2, l + 1):
            for j in range(1, min(i, l // 2 + 1)):
                need_value = j * avg
                for value in dp[i - 1][j]:
                    dp[i][j].add(value)
                    if abs(value - need_value) < 1e-8:
                        return True
                for value in dp[i - 1][j - 1]:
                    cur_value = value + A[i - 1]
                    dp[i][j].add(cur_value)
                    if abs(cur_value - need_value) < 1e-8:
                        return True
            dp[i - 1] = []
        return False

print(Solution().splitArraySameAverage([1,2,3,4,5,6,7,8]))
print(Solution().splitArraySameAverage([3,1]))
print(Solution().splitArraySameAverage([6,8,18,3,1]))
print(Solution().splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))
print(Solution().splitArraySameAverage([904,8738,6439,1889,138,5771,8899,5790,662,8402,3074,1844,5926,8720,7159,6793,7402,9466,1282,1748,434,842,22]))