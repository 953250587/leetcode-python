"""
On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting from the bottom left of the board, and alternating direction each row.  For example, for a 6 x 6 board, the numbers are written as follows:


You start on square 1 of the board (which is always in the last row and first column).  Each move, starting from square x, consists of the following:

You choose a destination square S with number x+1, x+2, x+3, x+4, x+5, or x+6, provided this number is <= N*N.
(This choice simulates the result of a standard 6-sided die roll: ie., there are always at most 6 destinations.)
If S has a snake or ladder, you move to the destination of that snake or ladder.  Otherwise, you move to S.
A board square on row r and column c has a "snake or ladder" if board[r][c] != -1.  The destination of that snake or ladder is board[r][c].

Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another snake or ladder, you do not continue moving.  (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at `3`, because you do not continue moving to `4`.)

Return the least number of moves required to reach square N*N.  If it is not possible, return -1.

Example 1:

Input: [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
Note:

2 <= board.length = board[0].length <= 20
board[i][j] is between 1 and N*N or is equal to -1.
The board square with number 1 has no snake or ladder.
The board square with number N*N has no snake or ladder.
"""
class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        line = []
        for i in range(len(board)):
            line.extend(board[-i - 1] if i % 2 == 0 else board[-i - 1][::-1])
        l = len(line)
        # 记忆数组，用来记录走过的位置到达目标点的最小移动次数
        memory = {}
        # 用来记录单次走过的路径，保证不会出现圈的情况
        used = set()
        def dfs(position, line):
            # print(position)
            # print(used)
            # print(memory)
            if position in memory:
                return memory[position]

            # 记录这次走的位置，在该次路径中不会再出现这个点
            used.add(position)

            min_value = float('inf')
            # 模拟色子情况，每次可以从1-6里选择一个执行
            for i in range(1, 7):
                t = min(position + i - 1, l - 1)
                if line[t] != -1:
                    # 判断跳格（或者不能跳格）的下一步的最少次数
                    move_position = line[t]
                else:
                    move_position = t + 1
                # 这个位置在这次循环中已经走过
                if move_position in used:
                    continue
                # 如果已经超过目标位置，则意味着结束该次模拟情况
                if move_position >= l:
                    temp = 0
                else:
                    temp = dfs(move_position, line)
                if temp != -1:
                    # 如果能够到达，则在之后的步数上+1
                    min_value = min(min_value, temp + 1)
            # 删除这次的路径节点
            used.remove(position)
            # 如果所有都不能够到达，则返回-1，并且用记录数组记录
            if min_value == float('inf'):
                memory[position] = -1
                return -1
            else:
                memory[position] = min_value
                return min_value
        # print([[i+1,j] for i,j in enumerate(line)])
        a = dfs(1, line)
        print(memory)

        return a

    def snakesAndLadders_1(self, board):
        """
        60ms BFS!!!!!
        :param board:
        :return:
        """
        n = len(board)
        need = {1: 0}
        bfs = [1]
        for x in bfs:
            for i in range(x + 1, x + 7):
                a, b = (i - 1) / n, (i - 1) % n
                nxt = board[~a][b if a % 2 == 0 else ~b]
                if nxt > 0: i = nxt
                if i == n * n: return need[x] + 1
                if i not in need:
                    need[i] = need[x] + 1
                    bfs.append(i)
        return -1

    def snakesAndLadders_2(self, board):
        """
        44ms
        :type board: List[List[int]]
        :rtype: int
        """
        import collections
        m, n = len(board), len(board[0])
        line, flip = [0], 0
        for i in range(m - 1, -1, -1):
            if flip:
                temp = board[i][::-1]
            else:
                temp = board[i]

            line += temp
            flip = flip ^ 1

        q = collections.deque([(1, 0)])
        visited = set([1])
        target = m * n
        while q:
            node, hop = q.popleft()

            for move in range(1, 7):
                nextloc = node + move

                if nextloc < len(line) and line[nextloc] != -1:
                    nextloc = line[nextloc]

                if nextloc < len(line) and nextloc not in visited:
                    visited.add(nextloc)
                    q.append((nextloc, hop + 1))
                    if nextloc == target: return hop + 1

        return -1
board = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(board))

board = [
[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
print(Solution().snakesAndLadders(board))

board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
print(Solution().snakesAndLadders(board))


board = [[-1,-1,2,-1],[14,2,12,3],[4,9,1,11],[-1,2,1,16]]
print(Solution().snakesAndLadders(board))