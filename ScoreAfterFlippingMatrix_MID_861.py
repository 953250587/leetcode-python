"""
We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.



Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39


Note:

1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""


class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        36 ms
        """
        temp_0 = []
        temp_1 = []
        for a in A:
            t = [abs(i - 1) for i in a]
            if a[0] == 0:
                temp_0.append(a)
                temp_1.append(t)
            else:
                temp_0.append(t)
                temp_1.append(a)
        l = len(A[0])
        max_length = len(A)
        ans = 0
        j = 0
        while j < l:
            t = sum([temp_0[i][j] for i in range(max_length)])
            s_0 = max(max_length - t, t)
            t = sum([temp_1[i][j] for i in range(max_length)])
            s_1 = max(max_length - t, t)
            if s_0 < s_1:
                while j < l:
                    ans += 2 ** (l - j - 1) * s_1
                    t = sum([temp_1[i][j] for i in range(max_length)])
                    s_1 = max(max_length - t, t)
                    j += 1
                    # print('0', ans)
            elif s_0 > s_1:
                while j < l:
                    ans += 2 ** (l - j - 1) * s_0
                    t = sum([temp_0[i][j] for i in range(max_length)])
                    s_0 = max(max_length - t, t)
                    j += 1
                    # print('1', ans)
            else:
                # print(s_0)
                ans += (2 ** (l - j - 1)) * s_0
                # print('3', ans)
            j += 1
        return ans

    def matrixScore_1(self, A):
        """
        38ms
        :param A:
        :return:
        """
        R, C = len(A), len(A[0])
        ans = 0
        for c in range(C):
            col = 0
            for r in range(R):
                col += A[r][c] ^ A[r][0]
            ans += max(col, R - col) * 2 ** (C - 1 - c)
        return ans
print(Solution().matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]))






