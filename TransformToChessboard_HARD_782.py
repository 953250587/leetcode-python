"""
An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

Examples:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.

Note:

    board will have the same number of rows and columns, a number in the range [2, 30].
    board[i][j] will be only 0s or 1s.


"""

class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        68ms
        """
        l = len(board)
        if not l // 2 <= sum(board[0]) <= l // 2 + l % 2: return -1
        if not l // 2 <= sum(board[i][0] for i in range(l)) <= l // 2 + l % 2: return -1
        mark_0 = None
        mark_1 = None
        for i in range(l):
            if board[i][0] == 0 and not mark_0:
                mark_0 = board[i][:]
            elif board[i][0] == 1 and not mark_1:
                mark_1 = board[i][:]
            if mark_0 and mark_1:
                break
        print(mark_1, mark_0)
        for i in range(l):
            if mark_0[i] + mark_1[i] != 1:
                return -1
        for i in range(l):
            mark = board[i][0]
            if mark == 0:
                for j in range(l):
                    if board[i][j] != mark_0[j]:
                        return -1
            else:
                for j in range(l):
                    if board[i][j] != mark_1[j]:
                        return -1


        col = sum(board[0][i] == i % 2 for i in range(l))
        row = sum(board[i][0] == i % 2 for i in range(l))
        if l % 2 == 0:
            col = min(col, l - col)
            row = min(row, l - row)
        else:
            if col % 2 == 1:
                col = l - col
            if row % 2 == 1:
                row = l - row
        return (col + row) // 2


print(Solution().movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]))