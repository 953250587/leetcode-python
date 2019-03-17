"""
On a 2 dimensional grid with R rows and C columns, we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column, and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid, we continue our walk outside the grid (but may return to the grid boundary later.)

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.



Example 1:

Input: R = 1, C = 4, r0 = 0, c0 = 0
Output: [[0,0],[0,1],[0,2],[0,3]]




Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]



Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C
"""


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        176MS
        """
        result = [[r0, c0]]
        k = 1
        while len(result) < R * C:
            if 0 <= r0 < R:
                for j in range(max(0, c0 + 1), min(c0 + 1 + k, C)):
                    result.append([r0, j])
            c0 = c0 + k
            print('1', r0, c0, k)
            if 0 <= c0 < C:
                for i in range(max(r0 + 1, 0), min(r0 + 1 + k, R)):
                    result.append([i, c0])
            r0 = r0 + k
            print('2', r0, c0, k)
            k += 1
            if 0 <= r0 < R:
                for j in range(min(C - 1, c0 - 1), max(c0 - 1 - k, -1), -1):
                    result.append([r0, j])
            c0 = c0 - k
            print('3', r0, c0, k)
            if 0 <= c0 < C:
                for i in range(min(R - 1, r0 - 1), max(r0 - 1 - k, -1), -1):
                    result.append([i, c0])
            r0 = r0 - k
            print('4', r0, c0, k)
            k += 1

        return result

    def spiralMatrixIII_1(self, R, C, r0, c0):
        """
        180ms
        :param R:
        :param C:
        :param r0:
        :param c0:
        :return:
        """
        ans = [(r0, c0)]
        if R * C == 1: return ans

        # For walk length k = 1, 3, 5 ...
        for k in range(1, 2 * (R + C), 2):

            # For direction (dr, dc) = east, south, west, north;
            # and walk length dk...
            for dr, dc, dk in ((0, 1, k), (1, 0, k), (0, -1, k + 1), (-1, 0, k + 1)):

                # For each of dk units in the current direction ...
                for _ in range(dk):

                    # Step in that direction
                    r0 += dr
                    c0 += dc

                    # If on the grid ...
                    if 0 <= r0 < R and 0 <= c0 < C:
                        ans.append((r0, c0))
                        if len(ans) == R * C:
                            return ans
# print(Solution().spiralMatrixIII(R = 1, C = 4, r0 = 0, c0 = 0))
print(Solution().spiralMatrixIII(R = 5, C = 6, r0 = 1, c0 = 4))
print(Solution().spiralMatrixIII(1, 1, 0, 0))



