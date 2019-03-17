"""
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

    If a mine ('M') is revealed, then the game is over - change it to 'X'.
    If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
    If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
    Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Example 2:

Input:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Explanation:

Note:

    The range of the input matrix's height and width is [1,50].
    The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
    The input board won't be a stage when game is over (some mines have been revealed).
    For simplicity, not mentioned rules should be ignored in this problem. For example, you don't need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

"""
import numpy as np
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        285ms
        """
        self.board = board
        r = len(board)
        if r <= 0:
            return []
        l = len(board[0])
        if self.board[click[0]][click[1]] == 'M':
            self.board[click[0]][click[1]] = 'X'
            return self.board

        self.stack = [click]
        def bfs(i, j):
            stack = []
            count_l = 0
            if self.board[i][j] != 'E':
                return []
            if i - 1 >= 0 and j - 1 >=0:
                if self.board[i - 1][j - 1] == 'E':
                    stack.append([i - 1, j - 1])
                elif self.board[i - 1][j - 1] == 'M':
                    count_l += 1
            if i - 1 >= 0:
                if self.board[i - 1][j] == 'E':
                    stack.append([i - 1, j])
                elif self.board[i - 1][j] == 'M':
                    count_l += 1
            if i - 1 >= 0 and j + 1 < l:
                if self.board[i - 1][j + 1] == 'E':
                    stack.append([i - 1, j + 1])
                elif self.board[i - 1][j + 1] == 'M':
                    count_l += 1
            if j - 1 >=0:
                if self.board[i][j - 1] == 'E':
                    stack.append([i, j - 1])
                elif self.board[i][j - 1] == 'M':
                    count_l += 1
            if j + 1 < l:
                if self.board[i][j + 1] == 'E':
                    stack.append([i, j + 1])
                elif self.board[i][j + 1] == 'M':
                    count_l += 1
            if i + 1 < r and j - 1 >=0:
                if self.board[i + 1][j - 1] == 'E':
                    stack.append([i + 1, j - 1])
                elif self.board[i + 1][j - 1] == 'M':
                    count_l += 1
            if i + 1 < r:
                if self.board[i + 1][j] == 'E':
                    stack.append([i + 1, j])
                elif self.board[i + 1][j] == 'M':
                    count_l += 1
            if i + 1 < r and j + 1 < l:
                if self.board[i + 1][j + 1] == 'E':
                    stack.append([i + 1, j + 1])
                elif self.board[i + 1][j + 1] == 'M':
                    count_l += 1
            if count_l != 0:
                self.board[i][j] = str(count_l)
                return []
            else:
                self.board[i][j] = 'B'
                return stack

        start = 0
        while start < len(self.stack):
            a = self.stack[start]
            self.stack.extend(bfs(a[0], a[1]))
            start += 1
            print(np.array(self.board))
            print(self.stack)
        return self.board

    def updateBoard_1(self, board, click):
        """
        355ms
        :param board:
        :param click:
        :return:
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        stack = [click]
        seen = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif board[x][y] == 'E':
                neigh = [(i, j) for i, j in (
                (x + 1, y + 1), (x + 1, y), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y + 1), (x - 1, y),
                (x - 1, y - 1)) if -1 < i < m and -1 < j < n]
                num = sum(board[i][j] == 'M' for i, j in neigh)
                board[x][y] = str(num) if num else 'B'
                if not num:
                    stack.extend(neigh)
        return board

board = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
click = [3,0]
print(Solution().updateBoard(board, click))

board = [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
click = [1,2]
print(Solution().updateBoard(board, click))