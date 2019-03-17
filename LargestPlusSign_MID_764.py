"""
 In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000

Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.

Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.

Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.

Note:

    N will be an integer in the range [1, 500].
    mines will have length at most 5000.
    mines[i] will be length 2 and consist of integers in the range [0, N-1].
    (Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)

"""
class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        4683 ms
        """
        import bisect
        dicts_row = {}
        dicts_col = {}
        max_1 = 0
        for mine in mines:
            key = mine[0]
            if key not in dicts_row:
                dicts_row[key] = set()
            dicts_row[key].add(mine[1])
            # bisect.insort_left(dicts_row[key], mine[1])

            key = mine[1]
            if key not in dicts_col:
                dicts_col[key] = set()
            dicts_col[key].add(mine[0])
            # bisect.insort_left(dicts_col[key], mine[0])
        for i in range(N):
            if i in dicts_row:
                dicts_row[i] = sorted(list(dicts_row[i]))
            if i in dicts_col:
                dicts_col[i] = sorted(list(dicts_col[i]))

        for i in range(N):
            for j in range(N):
                # print(i, j)
                row = dicts_row[i] if i in dicts_row else []
                col = dicts_col[j] if j in dicts_col else []
                a = bisect.bisect_left(row, j)
                if a - 1 < 0:
                    left = -1
                else:
                    left = row[a - 1]
                if a >= len(row):
                    right = N
                else:
                    right = row[a]
                # print(left, j, right)
                min_1 = min(j - left, right - j)
                b = bisect.bisect_left(col, i)
                if b - 1 < 0:
                    left = -1
                else:
                    left = col[b - 1]
                if b >= len(col):
                    right = N
                else:
                    right = col[b]
                min_2 = min(i - left, right - i)
                # print(left, i, right)
                max_1 = max(max_1, min(min_1, min_2))
        return max_1
# import bisect
# print(bisect.bisect_left([0,1,2,4], -1))
# print(bisect.bisect_left([0,1,2,4], 3))
# print(bisect.bisect_left([0,1,2,4], 5))
# print(bisect.bisect_left([], 1))
print(Solution().orderOfLargestPlusSign(N = 5, mines = [[4, 2]]))
print(Solution().orderOfLargestPlusSign(N = 2, mines = []))
print(Solution().orderOfLargestPlusSign(N = 1, mines = [[0, 0]]))

from bisect import bisect_right

class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        286ms
        """
        rows = [[-1, N] for _ in range(N)]
        cols = [[-1, N] for _ in range(N)]
        for r, c in mines:
            rows[r].append(c)
            cols[c].append(r)
        for i in range(N):
            rows[i].sort()
            cols[i].sort()
        mxp = 0
        for r in range(N):
            for i in range(len(rows[r])-1):
                left_b = rows[r][i]
                right_b = rows[r][i+1]
                for c in range(left_b+mxp+1, right_b-mxp):
                    idx = bisect_right(cols[c], r)-1
                    up_b = cols[c][idx]
                    down_b = cols[c][idx+1]
                    mxp = max(mxp, min(c-left_b, right_b-c, r-up_b, down_b-r))
        return mxp


