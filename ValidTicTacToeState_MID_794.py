"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

    Players take turns placing characters into empty squares (" ").
    The first player always places "X" characters, while the second player always places "O" characters.
    "X" and "O" characters are always placed into empty squares, never filled ones.
    The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
    The game also ends if all squares are non-empty.
    No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true

Note:

    board is a length-3 array of strings, where each string board[i] has length 3.
    Each board[i][j] is a character in the set {" ", "X", "O"}.

"""
class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        34ms
        """
        # 判断是否已经获胜
        def is_win(mark, board):
            left2right = ''
            right2left = ''
            target = mark * 3
            for i in range(3):
                # 一行都是
                if board[i] == target:
                    return True
                # 一列都是
                s = board[0][i] + board[1][i] + board[2][i]
                if s == target:
                    return True
                # 从左到右对角线
                left2right += board[i][i]
                # 从右到左对角线
                right2left += board[-1 - i][i]
            if left2right == target or right2left == target:
                return True
            return False

        count_X = 0
        count_O = 0
        # 统计X,O各自的个数
        for s in board:
            for char in s:
                if char == 'X':
                    count_X += 1
                elif char == 'O':
                    count_O += 1
        # 判断OX个数是否一致，一致的话需要判断X之前是不是已经赢了
        if count_O == count_X:
            mark = 'X'
        # 判断OX个数是否一致，X比O大一的话需要判断O之前是不是已经赢了
        elif count_X == count_O + 1:
            mark = 'O'
        # 否则两者差了2个以上，肯定错误
        else:
            return False
        # 这种情况一定能够成立
        if count_O < 3:
            return True
        return not is_win(mark, board)

    def validTicTacToe_1(self, board):
        """
        :type board: List[str]
        :rtype: bool
        145ms
        """
        def is_win(mark, board):
            left2right = ''
            right2left = ''
            target = mark * 3
            for i in range(3):
                # 一行都是
                if ''.join(board[i]) == target:
                    return True
                # 一列都是
                s = board[0][i] + board[1][i] + board[2][i]
                if s == target:
                    return True
                # 从左到右对角线
                left2right += board[i][i]
                # 从右到左对角线
                right2left += board[-1 - i][i]
            if left2right == target or right2left == target:
                return True
            return False

        dicts = {'X':[], 'O':[], ' ':[]}
        for i in range(3):
            for j in range(3):
                dicts[board[i][j]].append((i, j))
        new_board = [[' ' for _ in range(3)] for _ in range(3)]

        def dfs(count, dicts, new_board):
            flag = True
            # 判断是否已经到达目标状态
            for i in range(3):
                if ''.join(new_board[i]) != board[i]:
                    flag = False
                    break
            if flag:
                return True
            # 当前下的棋子
            if count % 2 == 0:
                mark = 'X'
            else:
                mark = 'O'

            before_mark = 'X' if mark == 'O' else 'O'
            # 判断上一个玩家是不是已经赢得比赛
            if is_win(before_mark, new_board):
                return False

            for i in dicts[mark]:
                new_board[i[0]][i[1]] = mark
                copy_dicts = {}
                copy_dicts['X'] = dicts['X'][:]
                copy_dicts['O'] = dicts['O'][:]
                copy_dicts[mark].remove(i)
                if dfs(count + 1, copy_dicts, new_board):
                    return True
                new_board[i[0]][i[1]] = ''

            return False

        return dfs(0, dicts, new_board)






print(Solution().validTicTacToe_1(["O  ", "   ", "   "]))
print(Solution().validTicTacToe_1(["XOX", " X ", "   "]))
print(Solution().validTicTacToe_1(["XXX", "   ", "OOO"]))
print(Solution().validTicTacToe_1(["XOX", "O O", "XOX"]))
print(Solution().validTicTacToe_1(["XXX","OOX","OOX"]))
print(Solution().validTicTacToe_1(["X X","OXX","OOO"]))
